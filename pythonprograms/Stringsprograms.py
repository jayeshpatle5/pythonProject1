# str1="Madam"
#
# rev=""
#
# for x in range(0,len(str1)):
#    rev=str1[x]+rev
# print(rev)
#
# if str1==rev:
#     print("Given string is palindrome")
# else:
#     print("Given string is not palindrome")

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = "Hello, World!"
# x=a[1]
# print(type(x))
# print(a[1])
#
# for x in "banana":
#   print(x , end ='')

# txt = "The best things in life are free!"
# x="free" in txt
# print("freeyf" in txt)
# print(type(x))

# txt = "The best things in life are free!"
# if "free" not in txt:
#   print("Yes, 'free' is present.")
# else :
#     print("free is not available")

b = "    Hello, World!    "

x=b.split(",")
print(x)
print(type(x))

m= "hello"
n=" world "

l=m+n
print(l)

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {} dollars for {} pieces of item {}."
print(myorder.format(quantity, itemno, price))

