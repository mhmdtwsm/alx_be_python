number = int(input("Enter a number to see its multiplication table:"))

for i in range(10):
    print(f"{number} * {1+i} = {number * (1+i)}")
