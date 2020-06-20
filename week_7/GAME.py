# 승부차기 게임
# 사용자가 1~6까지의 숫자를 입력한다
#   ㄴ 사용자의 입력값이 1~6사이가 아닌 경우 안내문구와 함께 다시 재입력받는다
# 사용자의 입력값과 랜덤 숫자가 다르면 +1점 / 같으면 -1점
# 5점이 되는경우 게임종료

import random

count = 0

while True:
    if count == 5:
        break
    com_num = random.randint(1, 6) # 컴퓨터 입력값
    user_num = int(input())        # 사용자 입력값

    if user_num < 1 and user_num > 6:
        print("다시 입력해주세요")
        continue

    if user_num != com_num:
        count = count + 1
    elif user_num == com_num:
        count = count - 1

    print("입력값", user_num)
    print("컴퓨터값", com_num)
    print("현재스코어", count)






