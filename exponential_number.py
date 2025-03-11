# Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        num_raised = num_1 ** num_2

        print(f"The first number raised to the second number is {num_raised:.2f}")
        break
    except ValueError:
        print("Error. Enter a valid number.")
        