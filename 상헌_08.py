r=open('vacabulary.txt','r')

for i in r:
    enter=i.split("\n")[0]
    word=enter.split(": ")[0]
    mean=enter.split(": ")[1]
    # print(mean)

    a=input(f"{mean}: ")

    if a==word:
        print("정답")
    else:
        print(f"{word}입니다.")
r.close()