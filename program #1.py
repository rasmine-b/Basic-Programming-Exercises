# Create a program that ask user to input 2 numbers. Print the bigger number.

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        if num_1 > num_2:
            print(f"The bigger number is {num_1:.0f}")
        elif num_1 < num_2:
            print(f"The bigger number is {num_2:.0f}")
        else:
            print("Enter a bigger number")
        break
    except ValueError:
        print("Error: Enter a valid number.")