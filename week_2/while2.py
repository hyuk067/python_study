# continue
#   ㄴ 뒤에 있는 소스를 더 이상 진행하지 않고 반복문의 처음으로 돌아간다

# break
#   ㄴ 반복문을 탈출 한다

count = 0

while True:

    count = count + 1
    if count == 5:
        continue
    if count == 10:
        break

    print(count)

