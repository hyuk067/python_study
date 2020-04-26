# selenium 모듈
# -> http 대체용

# 장점 : requests 모듈로 개발하기 힘든것을 짧은시간에 개발이 가능하다
# 단점 : requests 모듈보다는 느리다

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

driver.get('http://naver.com') # <<< 페이지 이동
print(driver.page_source) # html 소스는 변수명.page_source


# 경로
# 절대경로
# 상대경로
# .. << 이전폴더 / . << 현재폴더