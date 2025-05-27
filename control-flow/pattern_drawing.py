l = int(input("Enter the size of the pattern:"))
i = 1
while i <= l:
    for j in range(l):
        print("*", end="")
    print()
    i+=1
    # HELLO