# Check the Anagrams
# str1="Fresher"
# str2="Refresh

str1="Fresher"
str2="Refresh"

if(len(str1)!=len(str2)):
    print("The given string are not anagrams")
else:
   str1= str1.lower()
   str2= str2.lower()
   list1=list(str1).sort();
   list2=list(str2).sort();
   if(list1 is list2):
       print("The given string are anagrams")
   else:
       print("The given string are not anagrams")