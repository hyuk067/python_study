# 네이버 영화정보 가져오기
# HTML 가져오기

from selenium import webdriver
from bs4 import BeautifulSoup

page1 = webdriver.Chrome('./chromedriver')
page1.get('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(page1.page_source, 'html.parser')

# dt태그 안에 a태그들을 find로 크롤링

movie_info = {}

# {
#   영화제목1 : [페이지링크, 이미지주소],
#   영화제목2 : [페이지링크, 이미지주소],
#   영화제목3 : [페이지링크, 이미지주소],
#       .               .
#       .               .
#       .               .
# }

soup2 = soup.find('ul', class_='lst_detail_t1')
lis = soup2.find_all('li')

for li in lis:
    movie_info[li.a.img.get('alt')] = []
    movie_info[li.a.img.get('alt')].append(li.a.get('href'))
    movie_info[li.a.img.get('alt')].append(li.a.img.get('src'))
    # print(li.a.get('href'))    # 페이지링크
    # print(li.a.img.get('src')) # 이미지주소
    # print(li.a.img.get('alt')) # 영화제목

print(movie_info)

#print(soup2)

# find_all()
# 첫번째 인자값 : 태그
# 두번째 인자값 : class, id



