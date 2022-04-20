import os
import copy
import sqlite3
from pymongo import MongoClient


DATABASE_NAME = 'pubgdata'
COLLECTION_NAME = 'steam_data'
MONGO_URI = "mongodb+srv://whaleuser:tjddn-100@pubgdata.skatj.mongodb.net/pubgdata?retryWrites=true&w=majority"

DB_FILENAME = 'pubg_result.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

client = MongoClient(MONGO_URI)
pubg_db = client[DATABASE_NAME]
pubg_col = pubg_db[COLLECTION_NAME]

conn = sqlite3.connect(DB_FILEPATH)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS PUBG')
cur.execute('''
CREATE TABLE IF NOT EXISTS PUBG (
    _id VARCHAR NOT NULL PRIMARY KEY,
    map VARCHAR,
    rank INTEGER,
    zone VARCHAR,
    damage_causer_name VARCHAR,
    damage_reason VARCHAR,
    distance REAL,
    additional_info VARCHAR
)
''')

pubg_list = pubg_col.find({},{'_id':1, 'map':1, 'rank': 1, 'zone': 1, 'damage_causer_name': 1, 'damage_reason': 1,'distance': 1,'additional_info':1})
for pub in pubg_list :
    cur.execute(f'''
    INSERT OR IGNORE INTO PUBG 
    VALUES(
        "{pub['_id']}",
        "{pub['map']}",
        "{pub['rank']}",
        "{pub['zone']}",
        "{pub['damage_causer_name']}",
        "{pub['damage_reason']}",
        "{pub['distance']}",
        "{pub['additional_info']}"
    )
    ''')

conn.commit()