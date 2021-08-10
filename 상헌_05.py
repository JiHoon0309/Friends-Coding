def sum_digit(num):
    if num<1000:
        return num//100+(num//10)%10+num%10
    else:
        return num//1000

sum=0
for i in range(1,1001):
    sum+=sum_digit(i)
print(sum)