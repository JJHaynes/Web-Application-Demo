from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()  # reads .env

conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    dbname=os.getenv('DB_NAME'),
    sslmode='disable'  # or 'require' if using SSL
)

with conn.cursor() as cur:
    cur.execute('SELECT NOW()')
    print('DB connected at', cur.fetchone()[0])
conn.close()
