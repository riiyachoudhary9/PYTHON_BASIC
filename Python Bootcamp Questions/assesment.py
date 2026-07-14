total = 0

for i in range(1, 11):
     hours = int(input(f"Enter parking duration for car {i}: "))
     if (hours == 1):
        charge = 5
     else:
        charge = 5 + (hours - 1) * 3
        total += charge

print("Total earnings:", total)

