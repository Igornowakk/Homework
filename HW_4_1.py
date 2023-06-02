while True:
    number1 = input("Enter the first number: ")
    if number1 == "quit":
        print("End")
        break
    math_symbol = input("Enter the math symbol: ")
    if math_symbol == "quit":
        print("End")
        break
    number2 = input("Enter the second number: ")
    if number2 == "quit":
        print("End")
        break
    if math_symbol == "-":
        print(int(number1) - int(number2))
    elif math_symbol == "+":
        print(int(number1) + int(number2))
    elif math_symbol == "*":
        print(int(number1) * int(number2))
    elif math_symbol == "/":
        if int(number2) == 0:
            print("It is impossible to divide by zero.")
        if int(number2) != 0:
            print(int(number1) / int(number2))











