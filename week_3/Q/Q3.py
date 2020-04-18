# 함수명 : three_time(x)
#   ㄴ 1~첫번째 매개변수의값까지 3의 배수의 합을 구해서 리턴
# 첫번째 매개변수 : 몇까지 실행할지 입력

def three_time(x):
    sum = 0
    for i in range(1, x+1):
        if i % 3 == 0:
            sum = sum + i
    return sum

num = int(input())
tot = three_time(num)

print(tot)

