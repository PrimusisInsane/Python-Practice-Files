from cal import add, subtract, multiply, divide

num1 =int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print(add(num1, num2))
print(subtract(num1, num2))
print(multiply(num1, num2 ))
if num2  != 0:
    print(divide(num1, num2))
else:
    print("cannot divide by 0")