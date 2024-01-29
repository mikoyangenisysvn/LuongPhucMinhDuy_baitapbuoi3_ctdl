def reverse(lst):
    n = len(lst)
    for i in range(n // 2):
        other = n - i - 1
        lst[i], lst[other] = lst[other], lst[i]

    print(lst)

# Sử dụng hàm với một danh sách ví dụ
my_list = [1, 2, 3, 4, 5]
reverse(my_list)
