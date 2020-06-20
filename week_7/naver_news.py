import requests
from bs4 import BeautifulSoup

# 오늘 날짜 받아오기
from datetime import datetime
#datetime.today().strftime("%Y/%m/%d %H:%M:%S")
# YYYY/mm/dd HH:MM:SS 형태의 시간 출력
today = datetime.today().strftime("%Y%m%d")
# YYYYmmdd 형태의 시간 출력

r = requests.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date='+today)
bs = BeautifulSoup(r.text, 'html.parser')
soup1 = bs.find('ol', class_='ranking_list')

list = soup1.find_all('li')
#print(list) #잘 가지고 왔는지 채크

for i in list:
    print(i)
    soup2 = i.find('div', class_='ranking_thumb')
    soup3 = i.find('div', class_='ranking_lede')

    print(soup2)
    print(soup3)

    # print(soup2.a.get('title'))
    # print(soup2.a.img.get('src'))
    # print(soup3.get_text())



# 매일 뉴스기사 업데이트 될 수 있게 바꿀 것 (v)
# src 하고 안에 본분(회색글씨) 까지 같이 가져오기 (v)
# 이번주 일요일까지 충분히 가능 (v)
# 네이버 영화에 타이틀, 이미지 가져오기
# 코드리뷰

# 물어볼 내용
#   ㄴ 1. 태그의 태그 접근을 보다 더 간결하게 하는 법
#   ㄴ 2. for문의 범위를 soup으로 설정했을 때의 카운트가 이해가 안감(뉴스의경우 60이 나오는데 왜 60인지 모름)
#   ㄴ 3. 영화도 똑같이 하면 되는건 알겠는데 영화의 경우 2번를 이용하여 만들고 싶은데 그게 안됨
#   ㄴ 4. for문 안의 내용을 좀 더 간결하게 만드는 법

