# 자연수가 홀수인지 짝수인지 판별

number = int(input())  # input() 은 사용자에게 입력값을 받는다

# 조건이 명확 할 때는 elif를 사용하는게 좋다

if number % 2 == 0:
    print('입력하신 숫자는 짝수입니다')
elif number % 2 == 1:
    print('입력하신 숫자는 홀수입니다')
else:
    print('숫자가 아닙니다')

