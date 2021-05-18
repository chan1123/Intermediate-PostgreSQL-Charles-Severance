import psycopg2
import hidden
import time
import requests
import json

# Load the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS pokeapi
(id INTEGER, body JSONB);
'''
print(sql)
cur.execute(sql)

defaulturl = 'https://pokeapi.co/api/v2/pokemon/'
amount = int(input()) + 1
for i in range(1,amount):
  
    url = defaulturl + str(i)
    response = requests.get(url)
    text = response.text
    print(i)
    sql = 'UPDATE pokeapi SET id=%s, body=%s;'
    row = cur.execute(sql, (i, text))
#     print(text)

    time.sleep(2)
    
conn.commit()
cur.close()
