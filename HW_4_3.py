age = int(input("Enter age: "))

if age < 2:
    print("Baby")
elif age >= 2 and  age < 4:
    print("Kid")
elif age >= 4 and age < 13:
    print("Child")
elif age >= 13 and age < 20:
    print("Teenager")
elif age >= 20 and age < 65:
    print("Grown-up")
else:
    print("Senior")

