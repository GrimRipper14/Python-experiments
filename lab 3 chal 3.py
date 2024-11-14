# Zachary Boggs
# Lab 3 Challenge 3
# COP 2500C
# July 22, 2023
print("Welcome to the store.")


list=[]
for i in range(5):
    item=input("What would you like for item"+str(i+1)+"?\n")
    list.append(item.title())
    list.sort()


print("You have ordered:")

for i in range(5):
    print(str(i+1)+"."+list[i])
