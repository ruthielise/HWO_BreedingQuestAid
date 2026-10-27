DROP TABLE IF EXISTS breeding_partners;

CREATE TABLE breeding_partners (
    name TEXT PRIMARY KEY,
    crossbreed_bool TEXT,
    partner1 TEXT,
    partner2 TEXT
);
