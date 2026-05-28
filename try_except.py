try:
    number = int(input("Enter number: "))
    print (10/number)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("PLease enter a valid number")

    