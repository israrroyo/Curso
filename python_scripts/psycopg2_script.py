import psycopg2

conn = psycopg2.connect("dbname=beeva_test user=beeva password=beeva2014")

cur = conn.cursor()
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",

conn.commit()

cur.close()
conn.close()
