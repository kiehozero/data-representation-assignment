'''File to create tables, the same file as Andrew provided in lectures.'''
import pymysql
import config

db = pymysql.connect(
    host='localhost',
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)


# Create collection for user to store their players
def createCollection():
    cursor = db.cursor()
    col_table = '''CREATE TABLE collection (
        id INT AUTO_INCREMENT PRIMARY KEY,
        player_id INT,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        position VARCHAR(3),
        team VARCHAR(30),
        logo_url VARCHAR(250),
        headshot_url VARCHAR(250),
        gp INT,
        goals INT,
        assists INT,
        points INT,
        pim INT)'''

    cursor.execute(col_table)
    db.close()
    cursor.close()


# Create all_players table to store all players
def createPlayers():
    cursor = db.cursor()
    all_table = '''CREATE TABLE all_players (
        id INT AUTO_INCREMENT PRIMARY KEY,
        player_id INT,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        position VARCHAR(3),
        team VARCHAR(30),
        logo_url VARCHAR(250),
        headshot_url VARCHAR(250),
        gp INT,
        goals INT,
        assists INT,
        points INT,
        pim INT)'''

    cursor.execute(all_table)
    db.close()
    cursor.close()


# Query to create player IDs table
def createPlayerIds():
    cursor = db.cursor()
    pla_table = '''CREATE TABLE players (
        id INT AUTO_INCREMENT PRIMARY KEY,
        player_id INT)'''

    cursor.execute(pla_table)
    db.close()
    cursor.close()


if __name__ == '__main__':
    createCollection()
    createPlayers()
    createPlayerIds()
