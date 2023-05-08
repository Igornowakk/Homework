n = "Taras Shevchenko*1814-03-09*1861-03-10"
lst = (n.split("*"))
name = lst[0]
date1 = lst[1]
date2 = lst[2]
lst1 = (date1.split("-"))
lst2 = (date2.split("-"))
byear = lst1[0]
dyear = lst2[0]
age = int(dyear) - int(byear)


print("Name: ", name)
print("Age: ", age)
















