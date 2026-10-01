CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    active INTEGER NOT NULL
);

INSERT INTO users (id, name, email, active)
VALUES
    (1, 'Marko Markovic', 'marko@example.com', 1),
    (2, 'Ana Anic', 'ana@example.com', 1),
    (3, 'Petar Petrovic', 'petar@example.com', 0);