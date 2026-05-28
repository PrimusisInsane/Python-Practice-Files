mason_numbers = [85, 92, 60, 60, 92, 87]
mason_numbers.append(60)
task_force = {
    "name" : "Price",
    "age" : 46,
    "grade" : "Specialist"

}

average = sum(mason_numbers)/ len(mason_numbers)
what_numbers = set(mason_numbers)
print (f"The average is {average}")
print(mason_numbers[0])
print(what_numbers)
print(task_force["name"])
task_force["age"] = 45
print(task_force["age"])