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
