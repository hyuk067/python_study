#값을 다 가져와서
#어딘가에 저장
#어떤형태로 저장할지는 개발자 마음
#리스트 or 딕셔너리
#다음주부터 영어 진행
#수업을 늦게진행

import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")

#우선 값을 가져온다
#그걸 저장해야 하는데 뉴스의 경우 해당 날의 데이터를 끌어왔지만 얘는 해당 날짜가 없다
#예매, 개봉, 평점, 좋아요 순으로 내가 입력을 해서 입력 받은 값의 데이터를 뽑아온다
# https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=여기에 알맞는단어를 넣는데
# reserve = 예매 / open = 개봉 / point = 평점
# 가져올내용 : 영화제목, 개봉일, 평점, 이미지 src

# 우선 실행시키면 무조건 나와야 하는 내용
# ----- 원하는 순위방식의 번호를 입력 하세요 -----
# (다른 번호를 누르실 경우 예매순으로 보여드립니다)
# 1.예매 / 2.개봉 / 3.평점

# 리퀘스트.get을 이용해 해당 html소스를 가져온다
#r = requests.get('https://movie.naver.com/movie/running/current.nhn')

print('◆◇◆◇◆ 원하는 순위방식의 번호를 입력 하세요 ◆◇◆◇◆')
print('(다른 내용을 누르실 경우 예매순으로 보여드립니다)')
print('1.예매 / 2.개봉 / 3.평점')

# 사용자의 선택을 받아옴
user_sel = input()

# 사용자값에 따라 url 변경
# reserve = 예매 / open = 개봉 / point = 평점
if user_sel == '1':
    user_sela = 'reserve'
elif user_sel == '2':
    user_sela = 'open'
elif user_sel == '3':
    user_sela = 'point'
else:
    user_sela = 'reserve'

# 뷰티플숩을 이용해 해당 내용을 텍스트 형대로 만든다?
r = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order='+user_sela)
bs = BeautifulSoup(r.text, 'html.parser')

# 페이지 전체 내용 중에서 영화 리스트와 관련된 항복만 크롤링
totList = bs.find('ul', class_='lst_detail_t1')

# 리스트 부분을 전부 크롤링
totList1 = totList.find_all('li')

# 잘 가져왔는지 확인
#print(totList1)

movieList = []
count = 0

for i in totList1:

# 해당 내용 크롤링
    soup1 = i.find('div', class_='thumb')
    soup2 = i.find('dl', class_='lst_dsc')
    soup3 = soup2.find('span', class_='num')
    soup4 = soup2.find('dl', class_='info_txt1')

    movie_data = soup4.dd.get_text().replace("\n", "").replace("\t", "").replace("\r", "").split("|")

    addMovie = {
        '리스트인덱스' : count,
        '영화제목': soup2.dt.a.get_text(),
        '평점': soup3.get_text(),
        'src주소': soup1.a.img.get('src'),
        '개봉일' : movie_data[len(movie_data)-1]
    }
    count += 1
    movieList.append(addMovie)

print(movieList)