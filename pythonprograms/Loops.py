words = ['Jayesh','srikar','Vasanth','Yashmant']
for w in words :
    print(w,len(w))

#Code that modifies a collection while iterating over that same
#collection can be tricky to get right. Instead, it is usually more
#straight-forward to loop over a copy of the collection or to create a new collection:
users = {'Hans': 'active', 'Éléonore': 'inactive', 'Jayesh': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users,len(users))

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users, len(active_users))

for i in range(5):
    print(i)

list1=list(range(5, 10))
print(list1)

list2=list(range(0, 10, 3))
print(list2)

list3=list(range(-10, -100, -30))
print(list3)

a=['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

addition=sum(range(7))
print(addition)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)