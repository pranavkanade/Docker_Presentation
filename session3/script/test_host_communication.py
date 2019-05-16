import psycopg2 as pg
from pprint import pprint

try:
	connect_str = """dbname='tb_test' user='postgres' host='localhost'"""
	conn = pg.connect(connect_str)
except Exception as e:
	print("Error occured when connecting to database")
else:
	cursor = conn.cursor()
	cursor.execute("""select * from tab1""")
	rows = cursor.fetchall()
	pprint(rows)
