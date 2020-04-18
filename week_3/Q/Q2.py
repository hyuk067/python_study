# 함수명 : average
#   ㄴ 평균값을 출력시키는 함수
# 함수인자값 :  scoreList
# 점수리스트 ex) [30, 40, 50, 10]

def average(x):
    len(x)
    sum = 0
    for i in x:
        sum = sum + i

    res = sum / len(x)
    return res

scoreList = [30,40,50,10]

# 함수로부터 나온 결과값을 담아줄 수 있는 컵(tot)이 필요함
tot = average(scoreList)

print(tot)



