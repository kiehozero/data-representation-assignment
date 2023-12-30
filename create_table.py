'''File to create tables, the same file as Andrew provided in lectures.'''
import pymysql
import config

db = pymysql.connect(
    host='localhost',
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)

cursor = db.cursor()
# Query to create collection table
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

# Query to create players table
pla_table = '''CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT)'''

cursor.execute(pla_table)

db.close()
cursor.close()