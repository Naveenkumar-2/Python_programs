list=[1,2,3,4,5]
list1=[1,2,3,6]

for i in list1:
    if i not in list:
        list.append(i)
    

print(len(list))
