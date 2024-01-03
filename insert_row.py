'''Insert player manually to collection table just to test functionality'''
import config
import pymysql

db = pymysql.connect(
    host='localhost',
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)


def addAllPlayers():
    cursor = db.cursor()
    '''Using this method of writing a statement then adding each value later
    getting around potential injection attacks.'''
    sql_insert = '''INSERT INTO collection (player_id, first_name, last_name,
    position, team, logo_url, headshot_url, gp, goals, assists, points, pim)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

    # A collection of the first players returned from the API call
    vals = [
        (8476442, 'Matt', 'Nieto', 'L', 'Pittsburgh Penguins',
            'https://assets.nhle.com/logos/nhl/svg/PIT_light.svg',
            'https://assets.nhle.com/mugs/nhl/20232024/PIT/8476442.png',
            22, 1, 3, 4, 4),
        (8477846, 'Ryan', 'Carpenter', 'C', 'San Jose Sharks',
            'https://assets.nhle.com/logos/nhl/svg/SJS_light.svg',
            'https://assets.nhle.com/mugs/nhl/20232024/SJS/8477846.png',
            19, 1, 4, 5, 2)]

    for i in vals:
        cursor.execute(sql_insert, i)
        db.commit()
        print('1 player added to collection, ID:', cursor.lastrowid)

    db.close()
    cursor.close()


if __name__ == '__main__':
    addAllPlayers()
