votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

kim_count=0
kang_count=0
choi_count=0
for i in range(len(votes)):
    if votes[i]=='김영자':
        kim_count+=1
    elif votes[i]=='강승기':
        kang_count+=1
    else:
        choi_count+=1

vote_counter={"김영자":kim_count,"강승기":kang_count,"최만수":choi_count}
print(vote_counter)