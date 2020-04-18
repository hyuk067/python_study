# while 문을 사용해서 1부터 1000까지 자연수 중 3의 배수의 합을 구해서 출력




count = 0
sum = 0


while True:
    if count % 3 == 0:
        sum = sum + count
    elif count == 1000:
        break
    count = count + 1

print(sum)