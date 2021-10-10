import psycopg2
import csv

host='fanny.db.elephantsql.com'
database='eubqnbco'
user='eubqnbco'
password='UeqjvsMI0pllemGRM6jRmUI_tk8z7tGG'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database)

cur = connection.cursor()

#데이터를 테이블에 옮기기
cur.execute("DROP TABLE IF EXISTS mosquito_status;")
cur.execute("""CREATE TABLE mosquito_status (
				date VARCHAR(32),
                avg_temp FLOAT,
                min_temp FLOAT,
                max_temp FLOAT,
                precipitation FLOAT,
                mosquito_value_house FLOAT);
			""")

connection.commit()

query = """
    COPY mosquito_status FROM STDIN DELIMITER ',' CSV;
"""

with open('/Users/yunsu/seoul_mosquito_status_project/data/seoul_mosquito_status.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.copy_expert(query,f)

connection.commit()