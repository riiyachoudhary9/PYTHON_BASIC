print("Riya choudhary")

num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    sum += fact
    num = num // 10

if sum == original:
    print("Strong Number")
else:
    print("Not Strong Number")

print("Riya choudhary")