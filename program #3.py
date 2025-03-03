# Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        num_sum = num1 + num2
        print(f"The total sum of the 2 numbers is {num_sum:.2f}")
        break
    except ValueError:
        print("Error")