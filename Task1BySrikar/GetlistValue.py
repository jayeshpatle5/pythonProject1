# Remove the duplicates in following list using python code with out using set.
# list=["Grhombus", "Technologies", "Technologis", "GRhombus", "Technologies"]

list=["Grhombus", "Technologies", "Technologis", "GRhombus", "Technologies","Technologies"]
outputlist=[]
for i in range(0,len(list)):
    cond=True
    for j in range(i+1, len(list)):
        if(list[i]==list[j]):
            cond=False
            break
    if(cond):
        outputlist.append(list[i])
    cond=True

print(outputlist)