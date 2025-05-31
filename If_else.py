number = int(input("Enter a number :"))

if number <=1:
    print("Not a prime number")
else:
    for i in range(2,int(number ** 0.5)+1):
        if number % i ==0:
            print("Not a prime number")
            break
    else:
            print("Prime number")