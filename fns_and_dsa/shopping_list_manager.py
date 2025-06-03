def perform_operation(num1, num2, operation):
    """Perform Operations"""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Operation not valid can't divide on 0"
        return num1 / num2
