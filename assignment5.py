
l1 = []
for i in range(6):
    n=int(input('Enter list numbers: '))
    l1.append(n)
print(l1)
print("Sum of all the elements in list: ", sum(l1))
print("Find the smallest number: ",min(l1))
print("Find the largest number: ",max(l1))
l1.sort()
print("Display list in ascending order: ",l1)
l1.reverse()
print("Display list in descending order: ",l1)
t1=tuple(l1)
print("Display lis in tuple",t1)
del t1
print("List Deleted")