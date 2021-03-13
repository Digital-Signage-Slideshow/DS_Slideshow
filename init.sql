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