CREATE TABLE IF NOT EXISTS philosopher (
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    birth_year INTEGER NOT NULL,
    death_year INTEGER NOT NULL,
    school TEXT NOT NULL,
    catch_phrase TEXT
);