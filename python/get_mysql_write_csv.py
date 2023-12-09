import mysql.connector
import csv

host = '172.20.241.9'
user = 'dbaccess_ro'
password = 'vsdjkvwselkvwe234wv234vsdfas'
database = 'measurements'

dbQuery = 'SELECT * FROM measurements.rawdata where groupid = "13"'

db = mysql.connector.connect(host=host, user=user,
                             password=password, database=database)

cur = db.cursor()
cur.execute(dbQuery)

rows = cur.fetchall()

with open("C:/Koulu/Tvt22spl_syksy2023_projekti/python/data_from_mysql.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([i[0] for i in cur.description])
    writer.writerows(rows)