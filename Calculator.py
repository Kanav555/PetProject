# Sample Calculator 

# Program make a simple calculator

<<<<<<< HEAD
=======
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

>>>>>>> Release-1

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")



 # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
<<<<<<< HEAD
        num2 = float(input("Enter second number: "))
=======
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        else choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
>>>>>>> Release-1
