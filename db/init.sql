-- This is how the data should look like or in simple terms this creates tables 

CREATE TABLE events (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(), --Creating a unique id 
    event_type VARCHAR(100) NOT NULL, 
    payload JSONB NOT NULL,  -- The payload column is one column but can contain many pieces of information 
    status VARCHAR(100) NOT NULL DEFAULT 'pending', --Is the event processed or not 
    received_at TIMESTAMPZ DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMPZ, 
    retry_count INT DEFAULT 0
);


