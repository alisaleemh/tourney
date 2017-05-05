\c tournament ;

SELECT
  COALESCE(a.id, b.id) AS id,
  COALESCE(a.name, b.name) AS name,
  COALESCE(a.wins, 0) AS wins,
  COALESCE(b.losses, 0) AS losses
FROM
  (SELECT
    p.id AS id,
    p.name AS name,
    COUNT(m.winner) AS wins
  FROM
    players p,
    match m
  WHERE
    p.id = m.winner
  GROUP BY p.id) a FULL OUTER JOIN
  (SELECT
    p.id AS id,
    p.name AS name,
    COUNT(m.loser) AS losses
  FROM
    players p,
    match m
  WHERE
    p.id = m.loser
  GROUP BY p.id) b
  ON
    a.id = b.id
  ORDER BY wins DESC
;