num = int(input("Enter your number: "))

for number in range(num):
    if number ==20:
        break 
    print(number)

for number in range(num):
    if number ==2:
        continue
    print(number)
