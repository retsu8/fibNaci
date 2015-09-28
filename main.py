def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib.append(n)
        return fib(n-1)+fib(n-2)
    
fib = []
print fib(10)