# 사용방법

import schedule

def job():
    print("I'm working...")

# 10초에 한번씩 실행
schedule.every(1).seconds.do(job)


while True:
    schedule.run_pending()

