def printUnorderedPairs(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"{lst[i]},{lst[j]}")

# Sử dụng hàm với một danh sách ví dụ
my_list = [1, 2, 3]
printUnorderedPairs(my_list)
