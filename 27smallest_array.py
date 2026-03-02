print("Riya choudhary")

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)

print("Riya choudhary")