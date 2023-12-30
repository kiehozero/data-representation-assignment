'''Insert player manually to collection table just to test functionality'''
import pymysql
import config

db = pymysql.connect(
    host='localhost',
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)

cursor = db.cursor()
'''Using this method of writing a statement then adding each value later
getting around potential injection attacks.'''
sql_insert = '''INSERT INTO collection (player_id, first_name, last_name,
position, team, logo_url, headshot_url, gp, goals, assists, points, pim) VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

values = (8482468, 'Noah', 'Beck', 'D', 'St. Louis Blues',
          'https://assets.nhle.com/logos/nhl/svg/STL_light.svg',
          'https://assets.nhle.com/mugs/nhl/20232024/STL/8482468.png',
          9, 0, 3, 3, 4)

cursor.execute(sql_insert, values)

db.commit()
print('1 player added to collection, ID:', cursor.lastrowid)

db.close()
cursor.close()
