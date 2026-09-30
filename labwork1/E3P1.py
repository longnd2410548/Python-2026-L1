n = int(input("Enter a number: "))
if n <2:
    print (f"{n} is not a prime number")
else:
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
        else:
            prime = True
    if prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number") 
