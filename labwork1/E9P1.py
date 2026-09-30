def factorial(n):
    fac = 1
    for i in range(1,n+1,1):
        fac *= i
    return fac

n = int(input(print("enter a number: ")))
print (f"the factorial of {n}: ", factorial(n))
