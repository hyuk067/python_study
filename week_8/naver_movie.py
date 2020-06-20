
import pymysql
import schedule

import requests
from bs4 import BeautifulSoup

db = pymysql.connect(
        host='52.79.239.15',
        port=3306,
        user='asdf',
        passwd='asdf',
        db='study',
        charset='utf8')
cursor = db.cursor()

# 가져올내용 : 영화제목, 개봉일, 평점, 이미지 src

def job():

    # 뷰티플숩을 이용해 해당 내용을 텍스트 형대로 만든다?
    r = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
    bs = BeautifulSoup(r.text, 'html.parser')

    # 페이지 전체 내용 중에서 영화 리스트와 관련된 항복만 크롤링
    totList = bs.find('ul', class_='lst_detail_t1')

    # 리스트 부분을 전부 크롤링
    totList1 = totList.find_all('li')

    # 잘 가져왔는지 확인
    #print(totList1)

    movieList = []


    for i in totList1:

    # 해당 내용 크롤링
        soup1 = i.find('div', class_='thumb')
        soup2 = i.find('dl', class_='lst_dsc')
        soup3 = soup2.find('span', class_='num')
        soup4 = soup2.find('dl', class_='info_txt1')

        movie_data = soup4.dd.get_text().replace("\n", "").replace("\t", "").replace("\r", "").split("|")

        addMovie = {
            '영화제목': soup2.dt.a.get_text(),
            '개봉일' : movie_data[len(movie_data)-1],
            '평점': soup3.get_text(),
            'src주소': soup1.a.img.get('src')
        }
        movieList.append(addMovie)

    for i in movieList:
        sql = "SELECT * FROM naverMovie where title = %s"
        cursor.execute(sql, i['영화제목'])

        datas = cursor.fetchall()
        if len(datas) == 0:
            sql = "INSERT INTO naverMovie(title, date, score, img_src) values(%s, %s, %s, %s)"
            cursor.execute(sql, (i['영화제목'], i['개봉일'], i['평점'], i['src주소']))
        else:
            sql = "UPDATE naverMovie SET score = %s where title = %s"
            cursor.execute(sql, (i['평점'], i['영화제목']))

        db.commit()
    print("반복실행완료")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()

#1. 테이블 생성
#2. 데이터베이스 연동
#3. movieList만큼 돌면서 select 값을 가지고 와서
#   값이 있으면 update, 값이 없으면 insert 실행