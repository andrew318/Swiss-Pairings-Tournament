#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor = conn.cursor()
    query = """
        TRUNCATE TABLE matches;
        """
    cursor.execute(query)
    conn.commit()
    conn.close()  

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    query = """
        TRUNCATE TABLE players;
        """
    cursor.execute(query)
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT COUNT(*) FROM players;
        """
    cursor.execute(query)
    count = cursor.fetchall()
    conn.commit()
    conn.close()
    return count[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()

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
        Example: [
                    (id, name, wins, matches), 
                    (id, name, wins, matches)
                 ]
    """
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT players.id, players.name, count(players.name) as wins, count(matches.winner) as matches
                      FROM players, matches 
                      WHERE players.id = matches.winner 
                      GROUP BY players.id
                      ORDER BY wins desc;""")
    conn.commit()
    conn.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO matches VALUES (%s, %s);""", (winner, loser,))
    conn.commit()
    conn.close()
 
 
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

    conn = connect()
    cursor = conn.cursor()
    
    for (player in players):
        if (players.wins > players.wins):
            return ([player.id, player.id])

    cursor.execute()


    conn.commit()
    conn.close()
