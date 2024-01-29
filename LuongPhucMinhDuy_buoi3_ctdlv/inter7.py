def allFib(n):
    fib_list = [fib(i) for i in range(n)]
    for i, value in enumerate(fib_list):
        print(f"{i}: {value}")

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Sử dụng hàm với một số nguyên ví dụ
allFib(5)
