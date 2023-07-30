"""1"""
name = input("Enter name: ")
out_file = open("name.txt", "w")
out_file.write(name)

"""2"""
with open("name.txt", "r") as file:
    name = file.read()
    print(f"Your name is {name}")
out_file.close()

"""3"""
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    result = num1 + num2
    print(f"The sum of the first two numbers is {result}")

"""4"""
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(f"The total of all numbers is {total}")