# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

num_list = []
while True:
    try:
        for i in range (1,11):
            num = float(input(f"Enter a number{i}: "))
            num_list.append(num)

        num_sum = sum(num_list)
        print(f"The sum of all the numbers is {num_sum:.0f}")
        break
    except ValueError:
        print("Error.")