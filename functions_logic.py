def greet (name):
    return f"Hello {name}"
def calculate (marks):
    return f"Your average is {sum(marks)/len(marks)}"
s= 10  #global variable
def show():
    y = 15   #local variable inside a function
    print(s+y)
show()
message = greet(input("Enter your name: "))
average = calculate([56, 75, 90])
print (message)
print (average)
