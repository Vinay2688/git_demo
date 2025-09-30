def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)

n=int(input("enter n value"))
print("factorial of",n,"=",fact(n))
