\c tournament;

DROP TABLE IF EXISTS players CASCADE;
CREATE TABLE players (
  id serial primary key,
  name varchar(255) not null
);

DROP TABLE IF EXISTS match CASCADE;
CREATE TABLE match (
  id serial primary key,
  winner INT references players(id),
  loser INT references players(id)
);

CREATE OR REPLACE VIEW standings as
    SELECT
        p.id,
        p.name,
        COUNT(m.winner) as num_wins,
        COUNT(m.loser) as num_losses
    FROM
        players p,
        match m
    WHERE
        p.id = m.winner
    GROUP BY p.id
    ORDER BY num_wins DESC;
