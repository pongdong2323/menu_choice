import random

print("오징어 게임에 참가하셨습니다")
print("이번 게임은 다리 건너기 입니다")
# 오른쪽일까? 왼쪽일까?
print("오른쪽 왼쪽 중에 선택 하세요")
# 1번은 왼쪽 2번은 오른쪽
print("1번은 왼쪽 2번은 오른쪽")
# 총 10칸의 다리가 있다
# 왼쪽인지 오른쪽인 맞추면 살수 있고
# 틀리면 죽는다
# 최종 10칸까지 다가면 승리
# 중간에 틀리면 탈락 게임 오버
#num = int(input("선택하세요(숫자만): "))
#print("{}번으로 점프".format(num))
# 내 선택에 따라 살고 죽는다

for i in range(10):
    bridge =random.randint(0,1)
    print(bridge)

    num = int(input("선택하세요(1 or 0): "))

    print("{}번으로 점프".format(i+1))


    if bridge == num:
        print("통과")
        continue
        
    elif bridge != num: 
        print("으아아아악~")
        break
    
    if i == 10:
        print("살았다.")
        break
        