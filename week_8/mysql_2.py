import pymysql
#pymysql 인서트, 업데이트, 딜리트, 셀렉트

db = pymysql.connect(
        host='52.79.239.15',
        port=3306,
        user='asdf',
        passwd='asdf',
        db='study',
        charset='utf8')
cursor = db.cursor()



#===================SELECT===================
sql = "SELECT * FROM member"
cursor.execute(sql)

datas = cursor.fetchall()
for data in datas:
        print(data)

#===================INSERT===================
sql1 = "insert into member(id, pw, name) values(%s, %s, %s)"
cursor.execute(sql1, ('test3', '32132', 'c'))
db.commit()


#===================DELETE===================
sql2 = "DELETE FROM member where id=%s"
#cursor.execute(sql2, 'test3')
db.commit()

#===================UPDATE===================
sql3 = "UPDATE member SET id = 'test5' where no=%s"
cursor.execute(sql3, 17)
db.commit()

db.close()

# 19번째 줄의 datas = cursor.fetchall() 가 SETECT바로 다음에만 동작하는 이유는??

