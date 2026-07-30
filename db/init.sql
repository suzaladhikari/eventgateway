-- This is how the data should look like or in simple terms this creates tables 
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- This is the primary key 
    username VARCHAR(100),  -- Thi is where the user's names gets stored 
    email VARCHAR(255), -- This is where the email gets updated
    password VARCHAR(255) -- This is where the password gets updated
)