-- This is how the data should look like or in simple terms this creates tables 

CREATE TABLE events (
    event_id UUID PRIMARY KEY, --Creating a unique id 
    event_type VARCHAR(100) NOT NULL, 
    payload JSONB NOT NULL,  -- The payload column is one column but can contain many pieces of information 
    status VARCHAR(100) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'failed')), --Is the event processed or not 
    received_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMPTZ, 
    retry_count INT DEFAULT 0
);




