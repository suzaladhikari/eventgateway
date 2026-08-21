# EventGateway

Asynchronous event ingestion pipeline decoupling API request handling from data persistence, built on AWS with a FastAPI producer, SQS message queue, and independent worker service writing to PostgreSQL.

**API docs:** _(not publicly linked — see [Local Setup](#running-with-docker-recommended) or [Demo](#demo) below)_
**Source:** [github.com/suzaladhikari/eventgateway](https://github.com/suzaladhikari/eventgateway)

---

## Project Overview

EventGateway is a backend infrastructure project demonstrating how to decouple request handling from data processing using a message queue. Rather than writing directly to a database on every incoming request, a FastAPI producer validates and enqueues events to Amazon SQS and returns immediately — while a completely independent worker service polls the queue, processes messages, and persists them to PostgreSQL.

This pattern means the producer stays fast and available even if the worker is down, scaling, or slow — messages simply queue up and get processed once the worker recovers. The system also enforces least-privilege access at the infrastructure level: the producer's IAM role can only send to SQS, and has no path to the database at all, even in the event of a compromise.

---

## Architecture

```mermaid
flowchart TD
    A[Client] --> B[FastAPI Producer<br/>ECS Fargate]
    B -->|Validates payload<br/>Enqueues event| C[Amazon SQS]
    C -->|Durable buffer<br/>Decouples producer/consumer| D[Worker / Consumer<br/>ECS Fargate]
    D -->|Polls queue<br/>Processes message| E[RDS PostgreSQL]



1. Client sends a request to the FastAPI producer
2. Producer validates the payload against a Pydantic schema and pushes it to SQS via `boto3`, returning immediately (no waiting on downstream processing)
3. SQS holds the message durably until it's consumed
4. An independent worker service polls SQS, retrieves messages, and processes them
5. The worker writes the final record to RDS PostgreSQL via SQLAlchemy

---

## Key Design Decisions

- **Decoupled producer/consumer via SQS** — the two services never communicate directly. If the worker crashes or is scaling, the producer keeps accepting requests without failing.
- **Least-privilege IAM per service** — the producer's task role only grants `sqs:SendMessage`; it has zero permissions or network path to RDS. The worker's task role grants SQS read/delete plus DB access. Two task definitions, two separate blast radii.
- **Async response pattern** — the producer returns as soon as the event is queued, not after it's fully processed, keeping request latency low regardless of downstream load.
- **Environment-based configuration** — the same codebase reads `DATABASE_URL` from the process environment locally (via `.env` + `python-dotenv`) and from ECS task definition variables in production, with no code branching required.

---

## Tech Stack

- **Backend:** FastAPI, Pydantic
- **Messaging:** Amazon SQS (+ DLQ)
- **Database:** PostgreSQL (Amazon RDS), SQLAlchemy
- **Infrastructure:** Docker, Amazon ECS (Fargate), Amazon ECR, IAM
- **Observability:** Amazon CloudWatch Logs

---

## Challenges & Debugging

Deploying this to ECS surfaced three distinct failures across three different layers — each diagnosed from CloudWatch tracebacks rather than guesswork:

1. **Import-time crash in the producer.** A schema file had an unused import that transitively pulled in the database module, which called `create_engine()` at module load time with no `DATABASE_URL` set (correctly, since the producer shouldn't have DB access). Since Python imports execute eagerly, the app crashed before `uvicorn` could even start. Fixed by removing the dead import.

2. **Environment variable mismatch in the worker.** The worker's code read `os.getenv("RDS_DATABASE")`, but the ECS task definition only provided `DATABASE_URL`. Same class of bug, different variable name — the container had no config source for what the code expected. Fixed by aligning the code to the deployed environment's variable name.

3. **RDS authentication and SSL rejection.** After fixing the variable name, the worker still failed to connect — wrong master username baked into the connection string, and RDS rejecting unencrypted connections. Resolved by resetting the RDS master password, correcting the username, and appending `sslmode=require` to the connection string.

Each fix was verified in the live ECS environment: rebuilding and pushing new images to ECR, forcing service redeployments, and confirming end-to-end via CloudWatch logs and an actual SQS message count drop (queue depth going from 2 → 0 after the worker successfully processed and persisted both messages).

---

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)
- An AWS account with SQS, RDS, and ECR access (for full cloud deployment)

---

## Running with Docker (Recommended)

**1. Clone the repository**

```bash
git clone https://github.com/suzaladhikari/eventgateway.git
cd eventgateway
```

**2. Configure environment variables**

Copy `.env.example` to `.env` and fill in your local values:

```bash
cp .env.example .env
```

**3. Build and start the containers**

```bash
docker compose up --build
```

**4. Access the application**

| Service         | URL                          |
|-----------------|-------------------------------|
| FastAPI Docs    | http://localhost:8000/docs    |

**5. Stop all containers**

```bash
docker compose down
```

---

## Running Locally (Without Docker)

**1. Clone the repository**

```bash
git clone https://github.com/suzaladhikari/eventgateway.git
cd eventgateway
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Start the FastAPI producer**

```bash
uvicorn app.main:app --reload
```

**4. Start the worker** (in a new terminal)

```bash
python worker/consumer.py
```

---

## AWS Deployment

The producer and worker are deployed as separate Amazon ECS Fargate services, each with its own task definition, IAM task role, and security group:

| Component       | ECR Repo                  | ECS Service     |
|------------------|----------------------------|------------------|
| Producer         | `eventgateway-producer`    | `producer-svc`   |
| Worker           | `eventgateway-worker`      | `consumer-svc`   |

Deploying a code change requires rebuilding and pushing the Docker image to ECR, then forcing a new ECS deployment so the running service picks up the updated image:

```bash
aws ecs update-service \
  --cluster eventgateway-cluster \
  --service <service-name> \
  --force-new-deployment
```

---

## Project Structure
