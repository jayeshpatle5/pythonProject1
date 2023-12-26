# Reverse the String
# GRHoMbuS TechNloGies.
# Output = submohrG seigolnhceT

input='GRHoMbus TechNloGies'

list=input.split(' ')
output=''
for i in range(0,len(list)):
    temp=''
    for j in range(0,len(list[i])):
        str=list[i]
        if(j==0):
            temp=str[j].upper()+temp
        else:
            temp=str[j].lower()+temp

    output=output+temp+' '
print(output)