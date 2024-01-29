def factorial(n):
    # Kiểm tra nếu n là số âm
    if n < 0:
        return -1
    # Giai thừa của 0 là 1
    elif n == 0:
        return 1
    # Trường hợp n > 0
    else:
        # Sử dụng list comprehension để tính giai thừa
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Sử dụng hàm với một số nguyên ví dụ
result = factorial(5)
print(f"The factorial of 5 is: {result}")
