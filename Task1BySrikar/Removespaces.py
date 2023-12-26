# Remove the white spaces in below program
# str='a b c d e f'

str='a b c d e f'
output=''
for i in range(0,len(str)):
    if(str[i]!=' '):
        output=output+str[i]
print(output)