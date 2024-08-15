list1=[12,15,11,12,8,15,3,3]
print(list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
