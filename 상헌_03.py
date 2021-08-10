for a in range(400):
    for b in range(400):
        c=400-a-b
        if a*a+b*b==c*c and a<b<c:
            print(a*b*c)