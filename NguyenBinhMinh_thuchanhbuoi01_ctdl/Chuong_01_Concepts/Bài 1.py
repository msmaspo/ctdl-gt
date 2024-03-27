def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b, c = 0, 1, 0
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
        return c
    
n = int(input("Nhập một số nguyên n: "))

# Giải thuật đệ qui
fib_recursive = fibonacci_recursive(n)
print("Số Fibonacci (đệ qui):", fib_recursive)

# Giải thuật không đệ qui
fib_iterative = fibonacci_iterative(n)
print("Số Fibonacci (không đệ qui):", fib_iterative)