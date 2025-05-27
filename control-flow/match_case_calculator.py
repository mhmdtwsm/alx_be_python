num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number:"))

opt = input("Choose the operation (+, -, *, /):")

if opt == "+":
    print(f"The result is {num1 + num2}")
elif opt == "-":
    print(f"The result is {num1 - num2}")
elif opt == "*":
    print(f"The result is {num1 * num2}")
elif opt == '/':
    print(f"The result is {num1 / num2}")
