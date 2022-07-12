DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE album (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(100),
    artist_id INT NOT NULL REFERENCES artist(id)
);