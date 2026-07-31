-- Testing if the database is working or not 

-- Test One: Normal Successful payment event 
INSERT INTO events (event_id, event_type, payload, status, received_at, processed_at, retry_count)
VALUES (
    '11111111-1111-1111-1111-111111111111',
    'payment.completed',
    '{"amount": 4999, "currency": "usd", "customer_id": "cus_001", "payment_method": "card"}',
    'completed',
    now() - interval '10 minutes',
    now() - interval '9 minutes',
    0
);
-- Test Two: order created but still pending the processing 
INSERT INTO events (event_id, event_type, payload, status, received_at, processed_at, retry_count)
VALUES (
    '22222222-2222-2222-2222-222222222222',
    'order.created',
    '{"order_id": "ord_555", "items": 3, "total": 129.99, "customer_id": "cus_002"}',
    'pending',
    now() - interval '2 minutes',
    NULL,
    0
);

--Test Three: Subscription cancelled, failed after retires 

INSERT INTO events (event_id, event_type, payload, status, received_at, processed_at, retry_count)
VALUES (
    '33333333-3333-3333-3333-333333333333',
    'subscription.cancelled',
    '{"subscription_id": "sub_777", "customer_id": "cus_003", "reason": "payment_failed"}',
    'failed',
    now() - interval '30 minutes',
    NULL,
    3
);

-- Test Four: Another Payment being processed 
INSERT INTO events (event_id, event_type, payload, status, received_at, processed_at, retry_count)
VALUES (
    '44444444-4444-4444-4444-444444444444',
    'payment.completed',
    '{"amount": 1500, "currency": "usd", "customer_id": "cus_004", "payment_method": "paypal"}',
    'processing',
    now() - interval '1 minute',
    NULL,
    1
);
select * from events;


