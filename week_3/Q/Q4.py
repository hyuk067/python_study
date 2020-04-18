# abcde => "c"
# qwer => "we"

# 함수명 : solution(x)
#   ㄴ 문자열의 가운데 글자를 반환하는 함수
# 단어의 길이가 짝수면 두글자가 반환

# len 함수에 문자열을 넘기는경우 문자열의 길이를 리턴해줌
# 문자열 인덱싱을 사용해서 문제를 풀어야함

def solution(x):
    if len(x) % 2 == 1:
        print(x[len(x) // 2 : len(x) // 2+1])
    elif len(x) % 2 == 0:
        print(x[2])



solution(input())