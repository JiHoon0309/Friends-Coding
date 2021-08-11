import random

r=open('vacabulary.txt','r')

dic={}
for i in r:
    enter=i.split("\n")[0]
    word=enter.split(": ")[0]
    mean=enter.split(": ")[1]
    dic[word]=mean

while True:
    keys=list(dic.keys())
    ran=random.randint(0,len(keys)-1)
    # print(keys[ran])
    word=keys[ran]
    mean=dic[word]

    a=input(f"{mean}:")

    if a=='q':
        break
    if a==word:
        print("정답")
    else:
        print(f"틀렸습니다. 정답은 {word}입니다.")

