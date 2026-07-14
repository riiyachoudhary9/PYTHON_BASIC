# Print prime numbers from 1 to 100
count = 0
n=int(input("enter limit:"))

for num in range(2,n+1):      
    for i in range(2, num):    
        if num % i == 0:
            break              
    else:
        print(num)
        count= count+1
print("Total prime numbers =", count)
