print("Riya choudhary")

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = second = -999999

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)

print("Riya choudhary")