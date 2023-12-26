# Find the first repeating char in below string.
# str="abbcddeff"
# Output = b.

str="abbcddeff"
output=''
cond=True
for i in range(0,len(str)):
    for j in range(i+1, len(str)):
        if(str[i] is str[j]):
           output=str[i]
           cond=False
           break
    if(cond==False):
        break

print(output)