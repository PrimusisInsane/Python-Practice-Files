squares = {x * x for x in range(1,6)}
print(f"The squares of the following numbers are {squares}")

odd = int(input("Enter your number range:"))
odd_numbers = [x for x in range(odd) if x % 2 == 1]
print(f"The odd number between the number {odd} are {odd_numbers}")

square = lambda x: x * x    #useful for short operations, specially for sorting and filter
num = int(input("Enter your number: "))
print(square(num))

numbers = {12, 13, 14, 16, 18, 19}
squares = list(map(lambda x: x* x, numbers))   #map transforms each item in the list
evens = list(filter(lambda x: x % 2 == 0, numbers))   #filter sort out things that match the criteria
print(f"The squares are {squares}")
print(f"The evens are {evens}")

