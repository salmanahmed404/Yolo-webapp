import MySQLdb

db = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='Shaima@123',
        db='yolo_database'
    )
cursor = db.cursor()
cursor.execute('SELECT * FROM Yolo_city')
res = cursor.fetchall()
for val in res:
    print(str(val))