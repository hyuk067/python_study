from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')

id = 'id'
pw = 'pw'

sleep(0.5)
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")

sleep(0.5)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

sleep(0.5)
driver.find_element_by_xpath('//*[@id="PM_ID_ct"]/div[1]/div[2]/div[1]/ul[1]/li[1]/a').click()
driver.close()
