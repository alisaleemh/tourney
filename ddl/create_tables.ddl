\c tournament;

DROP TABLE IF EXISTS players CASCADE;
CREATE TABLE players (
  id serial primary key,
  name varchar(255) not null
);

DROP TABLE IF EXISTS match CASCADE;
CREATE TABLE match (
  id serial primary key,
  winner INT references players(id) ON DELETE CASCADE CHECK (winner <> loser),
  loser INT references players(id) ON DELETE CASCADE CHECK (winner <> loser)

);

CREATE OR REPLACE VIEW standings as
  SELECT
    COALESCE(a.id, b.id) AS id,
    COALESCE(a.name, b.name) AS name,
    COALESCE(a.wins, 0) AS wins,
    (a.wins + b.losses) AS matches
    --COALESCE(b.losses, 0) AS losses
  FROM
    (SELECT
      p.id AS id,
      p.name AS name,
      COUNT(m.winner) AS wins
    FROM
      players p FULL OUTER JOIN
      match m
    ON
      p.id = m.winner
    GROUP BY p.id) a FULL OUTER JOIN
    (SELECT
      p.id AS id,
      p.name AS name,
      COUNT(m.loser) AS losses
    FROM
      players p FULL OUTER JOIN
      match m
    ON
      p.id = m.loser
    GROUP BY p.id) b
    ON
      a.id = b.id
    ORDER BY wins DESC
;
