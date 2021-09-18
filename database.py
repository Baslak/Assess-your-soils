import psycopg2
import os 

DB_VINPROOF_NAME=os.environ.get('DATABASE_URL', "dbname=vinproof_db") 

def sql_select(query, params):
  conn = psycopg2.connect(DB_VINPROOF_NAME)
  cur = conn.cursor()
  cur.execute(query, params)
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results

def sql_write(query, params):
  conn = psycopg2.connect(DB_VINPROOF_NAME)
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  conn.close()