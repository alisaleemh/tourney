
from tournament import *

deleteMatches()
deletePlayers()
registerPlayer("Bruno Walton")
registerPlayer("Boots O'Neal")
registerPlayer("Cathy Burton")
registerPlayer("Diane Grant")
standings = playerStandings()
reportMatch(17, 18)
reportMatch(20, 19)
[id1, id2, id3, id4] = [row[0] for row in standings]
standings = playerStandings()
