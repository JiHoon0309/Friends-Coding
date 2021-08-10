prices=[34000,13000,5000,21000,1000,2000,8000,3000]
def krw_to_usd(prices):
    usd=prices/1000
    return usd
def usd_to_jpy(usd_list):
    jpy=((1000/8)*usd_list)
    return jpy

i=0
j=0
usd_list=[]
jpy_list=[]
while i<len(prices):
    usd_list.append(krw_to_usd(prices[i]))
    i+=1

while j<len(usd_list):
    jpy_list.append(usd_to_jpy(usd_list[j]))
    j+=1

print("한국 화폐:",prices)
print("미국 화폐:",usd_list)
print("일본 화폐:",jpy_list)