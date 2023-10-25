point = int(input("득점을 입력하시오"))
assist = int(input("어시를 입력하시오"))
block = int(input("블록을 입력하시오"))
steal = int(input("스틸을 입력하시오"))
rebound = int(input("리바운드를 입력하시오"))

player = [point, assist, block, steal, rebound]

def effi (player):
    A=[]
    for p in player:
        if p >=10:
            A.append(0)
    return A
B = effi (player)

if len(B) == 2:
    print("더블더블입니다.")
elif len(B) == 3:
    print("트리플더블입니다")
elif len(B) == 4:
    print("쿼드러블입니다.")
elif len(B) == 5:
    print("농구의 신 입니다.")
else:
    print("분발하세요!!")
