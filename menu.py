import random

print("오늘 점심 머 먹지?")
# 메뉴 리스트를 만들어보자
menu = ["짜장면", "짬뽕", "라면", "김밥", "돈까스"]
print(menu)
for i in menu:
    print(i)
print("이 중에서 엄청난 알고리즘으로 당신의 머릿속을 분석하여 추천하는 메뉴는? ")
print("두구 두구 두구 두구~~~~")
a = random.randint(0, 4)
print("{} 입니다".format(menu[a]))