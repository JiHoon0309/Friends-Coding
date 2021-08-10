def fahrenheit_to_celsius(fahrenheit):
    celsius=((fahrenheit-32)*5)/9
    return celsius
i=0
fahrenheit_list = [40, 15, 32, 64, -1, 11]
celsius_list=[]
while i < len(fahrenheit_list):
    celsius_list.append(round(fahrenheit_to_celsius(fahrenheit_list[i]),1))
    i+=1
print("화씨 온도 리스트:",fahrenheit_list)
print("섭씨 온도 리스트:",celsius_list)
