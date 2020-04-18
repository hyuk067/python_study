import requests
from bs4 import BeautifulSoup


for i in range(900, 907):
    r = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(i))

    soup = BeautifulSoup(r.text, 'html.parser')
    soup2 = soup.find('div', class_='num win')
    soup3 = soup.find('div', class_='num bonus')

    # find_all()
    # 첫번째 인자값 : 태그
    # 두번째 인자값 : class, id

    spans = soup2.find_all('span')
    spans2 = soup3.find('span')

    numbers = []

    for span in spans:
        numbers.append(span.text)

    print(numbers)
    print(spans2.text)

#   과제 덮어쓰기가 되는 numbers 리스트를 각각 다르게 저장할 코드 작성
#   딕셔너리, 리스트 활용