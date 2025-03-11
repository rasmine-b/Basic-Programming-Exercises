# Create a program that ask user to input 2 numbers. Print Equal when the numbers are the same.

while True: 
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        if num_1 == num_2:
            print("Equal")
        break
    except ValueError:
        print("Error: Enter a valid number.")