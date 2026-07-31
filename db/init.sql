-- This is how the data should look like or in simple terms this creates tables 

CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    eventype VARCHAR(100) NOT NULL
);



