# Create a program that ask user to input 2 numbers. Print the product of the two numbers.

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        num_product = num_1 * num_2

        print(f"The product of the 2 numbers is {num_product:.2f}")
        break
    except ValueError:
        print("Error. Enter a valid number.")