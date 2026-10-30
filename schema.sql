DROP TABLE IF EXISTS breeding_partners;

CREATE TABLE breeding_partners (
    name TEXT PRIMARY KEY,
    crossbreed_bool TEXT,
    partner1 TEXT,
    partner2 TEXT
);

DROP TABLE IF EXISTS quest_cascade;

CREATE TABLE quest_cascade (
    name TEXT PRIMARY KEY,
    unlocks_bool TEXT,
    unlocked_by TEXT,
);
