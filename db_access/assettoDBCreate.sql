CREATE TABLE server (
    id INTEGER PRIMARY KEY,
    name TEXT,
    pass TEXT,
    practice INTEGER,
    quali INTEGER,
    race INTEGER
);

CREATE TABLE track (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    variant TEXT,
    country TEXT,
    path TEXT
);

CREATE TABLE car (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    brand TEXT,
    model TEXT,
    skins TEXT,
    power FLOAT,
    weight INTEGER,
    country TEXT,
    year INTEGER,
    path TEXT
);

CREATE TABLE carList (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT
);

CREATE TABLE carListJoin (
    car INTEGER REFERENCES car,
    carList INTEGER REFERENCES carList,
    PRIMARY KEY(car, carList)
);

INSERT  OR REPLACE into car (brand, name, skins, power, weight, country, year, path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)