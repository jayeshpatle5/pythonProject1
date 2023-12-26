# Reverse the below string without changing it's position.
# str="I am  a software engineer!"
# Output = I ma a erawtfos !reenigne

str="I am a software engineer!"
list=str.split(" ")
Output =""
for i in range(0,len(list)):
    temp=""
    for j in range(0,len(list[i])):
        temp=list[i][j]+temp
    Output=Output + temp + " "

print(Output)