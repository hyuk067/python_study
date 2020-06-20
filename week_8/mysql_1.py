import pymysql

db = pymysql.connect(
        host='52.79.239.15',
        port=3306,
        user='asdf',
        passwd='asdf',
        db='study',
        charset='utf8')

cursor = db.cursor(pymysql.cursors.DictCursor)

sql = "CREATE TABLE student(name VARCHAR(8) NOT NULL, " \
                            "birth INT(8), " \
                            "team VARCHAR(10), " \
                            "phone VARCHAR(11), " \
                            "address VARCHAR(5))"

#for s in sql:
cursor.execute(sql)
db.commit()
db.close()
#result = cursor.fetchall()
#for r in result:
#print(r)

