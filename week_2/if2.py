# if 조건:
# elif 다른조건:
# else : ( 위 조건이 한가지도 부합하지 않는 경우에 실행 )

# elif와 else는 필수가 아니다
# 조건문이 부합하는 순간 뒤에 소스는 실행되지 않는다

money = 25000

if money > 50000:
    print('하고싶은거 다 해')
elif money > 20000:
    print('찜질방')
elif money > 10000:
    print('PC방')
else:
    print('편의점')

