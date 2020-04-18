# 집합 자료형
# 집합을 정의 시 set([값1, 값2, 값3])

s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6, 7])

print(s1 & s2) # 교집합
print(s1 | s2) # 합집합
print(s1 - s2) # 차집합
print(s2 - s1) # 차집합
