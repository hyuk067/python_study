# requests : HTTP 요청을 보낼 수 있는 모듈

# pip install 모듈명
# 모듈명은 제각각 다름
# import 모듈명 << 모듈을 불러올때 1
# from 함수명 import 모듈명 << 모듈을 불러올때 2


import requests
from bs4 import BeautifulSoup

# .get, .post
# 첫번째 인자는 URL
# 두번째 인자는 파라미터


r = requests.get('http://naver.com')

# 첫번째 인자는 HTML소스
# 두번째 인자는 'html.parser'
soup = BeautifulSoup(r.text, 'html.parser')

# find()
# 첫번째 인자값 : 태그명
# 두번째 인자값 : class_='클래스명'
#               id = 'id명'
print(soup.find('div', id='vata_top'))

# 변수명.text
print(soup.find('a'))

# 결과값은 코드 번호로 나타남



