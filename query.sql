\c tournament ;

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
