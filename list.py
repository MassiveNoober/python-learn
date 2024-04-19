list1 = [1,2 ,3 ,4, 5]

print(list1, sep = " ")

#different ways to add to list.
#list1.insert(len(list1), 6)
#list1.append(6)
#list1.extend([6, 7 ,8 ,9])

#different ways to delete from list
#list1.pop(4) this uses index so the 5 is removed
del list1[2] #like this the 3 is removed.

for x in list1:
    print('Value: ',x)
