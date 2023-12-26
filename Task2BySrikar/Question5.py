# Write character frequency program for given below string.
# Str = "aabbcccddeeeeffg";
# output = a=2, b=2, c=3, d=2, e=4, f=2, g=1;

Str = "aabbcccddeeeeffg"

diction={}

for x in Str :
    if(diction.__contains__(x)):
        diction[x]=diction[x]+1
    else:
        diction[x]=1

print(diction)