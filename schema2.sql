DROP TABLE IF EXISTS quest_cascade;

CREATE TABLE quest_cascade (
    name TEXT PRIMARY KEY,
    unlocks_bool TEXT,
    unlocked_by TEXT,
);
