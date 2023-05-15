number = int(input("Enter a number greater than zero: "))

if number == 0:
    print("The number must be greater than zero.")
else:
    produkt_of_number = 1

    while number > 0:
        digit = number % 10
        produkt_of_number *= digit
        number //= 10

    while produkt_of_number > 9:
        produkt_of_number2 = 1
        while produkt_of_number > 0:
            digit2 = produkt_of_number % 10
            produkt_of_number2 *= digit2
            produkt_of_number //= 10
        produkt_of_number = produkt_of_number2

    print("The produkt digitals of number is: ", produkt_of_number)

