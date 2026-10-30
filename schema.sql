PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS philosopher (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    birth_year INTEGER NOT NULL,
    death_year INTEGER NOT NULL,
    school TEXT NOT NULL,
    catch_phrase TEXT,
    CHECK(birth_year <= death_year)
);

CREATE TABLE IF NOT EXISTS argument (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    philosopher_id INTEGER NOT NULL,
    FOREIGN KEY (philosopher_id) REFERENCES philosopher (id) ON DELETE CASCADE,
    UNIQUE(philosopher_id, name)
);

CREATE TABLE IF NOT EXISTS arg_connection (
    id INTEGER PRIMARY KEY,
    relation_type TEXT NOT NULL CHECK(relation_type IN ('based_on', 'challenges', 'refutes')),
    source_arg_id INTEGER NOT NULL,
    target_arg_id INTEGER NOT NULL,
    FOREIGN KEY (source_arg_id) REFERENCES argument (id) ON DELETE CASCADE,
    FOREIGN KEY (target_arg_id) REFERENCES argument (id) ON DELETE CASCADE,
    UNIQUE(relation_type, source_arg_id, target_arg_id),
    CHECK(target_arg_id != source_arg_id)
);
