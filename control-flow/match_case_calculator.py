num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number:"))

opt = input("Choose the operation (+, -, *, /):")

match opt:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        print(f"The result is {num1 / num2}")
    case _:
        print("Invalid operation")
