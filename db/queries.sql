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
select * from events;