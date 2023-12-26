# Remove the Junk and add the sum of the numbers in given string.
# str="@33!@#Srikar!@!@#$%^&*(*()"
# Output= 6Srikar

name = "@33!@#Srikar!@!@#$%^&*(*()"


sum=0
temp=""
for char in name:
    if char.isdigit():
        sum+=int(char)
    elif char.isalpha():
        temp=temp+char

output=str(sum)+temp
print(output)
