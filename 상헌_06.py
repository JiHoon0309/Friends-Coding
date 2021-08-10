import random

ran=random.randrange(1,21)

for i in range(4):
    a=int(input(f"기회가 {4-i}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:"))
    if a>ran:
        print('down')
    elif a<ran:
        print('up')
    elif a==ran:
        print(f'축하합니다. {i+1}번 만에 숫자를 맞히셨습니다.')
        break
if a!=ran:
    print(f'아쉽습니다. 정답은 {ran}였습니다.')