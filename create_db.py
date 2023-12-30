'''File to create initial DB, the same file as Andrew provided in lectures.'''
import pymysql
import config

db = pymysql.connect(
    host='localhost',
    user=config.keys['user'],
    password=config.keys['pw']
)

cursor = db.cursor()
sql_create = 'CREATE DATABASE nhl_tt'
cursor.execute(sql_create)

db.close()
cursor.close()
