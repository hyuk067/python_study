# while : 반복문
# while 조건:

# while의 문제는 조건이 명확하지 않으면 무한루프에 빠진다
#   ㄴ 개발자의 의도에 따라서 무한루프를 만드는 경우도 있긴 하다

count = 0
while count < 10:
    count = count + 1
    print('Hello')
