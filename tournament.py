#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def readFile(file):
    file_obj = open(file, 'r')
    return file_obj.read()


def deleteMatches():
    """Remove all the match records from the database."""
    dbh = connect()
    cur = dbh.cursor()
    query = readFile('sql/delete_matches.sql')
    print query
    cur.execute(query)
    dbh.commit()
    dbh.close()


def deletePlayers():
    dbh = connect()
    cur = dbh.cursor()
    query = readFile('sql/delete_players.sql')
    print query
    cur.execute(query)
    dbh.commit()
    dbh.close()


def countPlayers():

    """Returns the number of players currently registered."""

    dbh = connect()
    cur = dbh.cursor()
    query = readFile('sql/count_players.sql')
    cur.execute(query)
    count = cur.fetchone()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    dbh = connect()
    cur = dbh.cursor()

    try:
        query = "INSERT INTO PLAYERS (name) VALUES (%s)"
        cur.execute(query, (name,))
    except psycopg2.Error as error:
        print "Failed to insert | registerPlayer() at line 65"
        print error.pgerror

    try:
        dbh.commit()
    except:
        print "Failed to commit | registerPlayer()"
        dbh.rollback()
    dbh.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    dbh = connect()
    cur = dbh.cursor()

    query = "SELECT * FROM standings"
    cur.execute(query)
    return cur.fetchall()


    dbh.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    dbh = connect()
    cur = dbh.cursor()

    if int(winner) == int(loser):
        return

    try:
        query = "INSERT INTO MATCH (winner, loser) VALUES (%s, %s)"
        params = (int(winner), int(loser))
        cur.execute(query, params)
    except psycopg2.Error as error:
        print "Failed to insert | registeMatch()"
        print error.pgerror

    try:
        dbh.commit()
    except:
        print "Failed to commit | reportMatch()"
        dbh.rollback()
    dbh.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
