# Added the below values to Dictionary and print line by line
# keys="name","Surname","Design","EmpID"  values="srikar","RB", "Software Engineer", 325269

thisdict = {
  "name": "srikar",
  "Surname": "RB",
  "Design": "Software Engineer",
  "EmpID": 325269
}

for x in thisdict:
    print(x, thisdict[x])