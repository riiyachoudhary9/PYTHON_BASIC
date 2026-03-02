print("Riya choudhary")

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter element to search: "))
found = False

for i in range(n):
    if arr[i] == key:
        print("Found at position", i+1)
        found = True
        break

if not found:
    print("Element not found")

print("Riya choudhary")