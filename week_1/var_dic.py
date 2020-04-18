# 딕셔너리는 키('apple')와 벨류(3000)가 쌍으로 이루어져있다
#  ㄴ JSON과 같은 형태를 가지고 있다
# 딕셔너리는 선언시 중괄호 {} 가지고 선언
# 딕셔너리도 값을 접근 할 때는 대괄호 [] 를 이용
#  ㄴ 대괄호 안에 값은 인덱스가 아닌 키값을 입력한다

fruitList = {
    'pineapple' : 5000,
    'orange' : 2000,
    'apple' : 3000,
    'banana' : 1000
}

print(fruitList['apple'])
