# 주어진 자연수가 홀수인지 짝수인지 판별
# 함수명 : is_odd

# input() : 사용자에게 입력값을 받는 함수
# int() : 정수로 형 변환을 해준다
# str() : 문자열로 형변환을 해준다

# 함수 정의시 함수의 기능은 명확해야한다
# 함수를 만드는 가장 큰 이유는 재사용에 있다

def is_odd(x):
    if x % 2 == 0:
        print("짝")
    elif x % 2 == 1:
        print("홀")

number = int(input())
is_odd(number)


