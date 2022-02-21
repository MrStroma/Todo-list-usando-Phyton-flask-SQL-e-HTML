DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);

INSERT INTO posts (titolo, info ) VALUES(
    'Studiare Python',
    'Studiare il linguaggio, la sintassi e la logica di tale linguaggio'
);

INSERT INTO posts (titolo, info ) VALUES(
    'Studiare Javascript',
    'Studiare il linguaggio, la sintassi e la logica di tale linguaggio'
);

INSERT INTO posts (titolo, info ) VALUES(
    'Studiare C',
    'Studiare il linguaggio, la sintassi e la logica di tale linguaggio'
);