# Create a program that ask user to input 2 numbers. Print the product of the two numbers.

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        num_product = num1 * num2
        print(f"The product of the 2 numbers is {num_product:.2f}")
        break
    except ValueError:
        print("Error.")