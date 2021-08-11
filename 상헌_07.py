f=open("vacabulary.txt",'w')

while True:
    word=input("영어 단어를 입력하세요: ")
    if word=='q':
        break

    mean=input("한국어 뜻을 입력하세요: ")
    if mean=='q':
        break

    f.write(f"{word}: {mean}\n")
f.close()