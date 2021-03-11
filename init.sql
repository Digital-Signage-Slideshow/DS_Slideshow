CREATE TABLE users (
    id SERIAL,
    created_on TIMESTAMP,
    updated_on TIMESTAMP,
    username VARCHAR(255) UNIQUE NOT NULl,
    password VARCHAR NOT NULL,
    active BOOLEAN,
    email VARCHAR(120),
    slug VARCHAR(120),
    PRIMARY KEY (id)
);

CREATE TABLE content (
    path VARCHAR(255) NOT NULL,
    priority INT UNIQUE,
    type VARCHAR(4),
    PRIMARY KEY(path)
);

INSERT INTO users(
    created_on, 
    updated_on, 
    username, 
    password, 
    active, 
    email, 
    slug
) VALUES(
    '01-01-2000', 
    '01-01-2000', 
    'admin', 
    'password', 
    TRUE, 
    'admin@admin.com', 
    'admin'
);