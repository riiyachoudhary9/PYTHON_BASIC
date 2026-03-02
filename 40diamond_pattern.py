print("Riya choudhary")

n = int(input("Enter number of rows: "))

# Upper pyramid
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

# Lower pyramid
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

print("Riya choudhary")