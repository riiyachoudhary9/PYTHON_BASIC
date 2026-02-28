print("Riya choudhary")

num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit*digit*digit
    num = num // 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")

print("Riya choudhary")