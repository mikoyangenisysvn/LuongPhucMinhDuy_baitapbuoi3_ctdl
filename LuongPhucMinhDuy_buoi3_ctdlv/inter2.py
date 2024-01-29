def printPairs(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            print(str(lst[i]) + "," + str(lst[j]))

# Sử dụng hàm với một danh sách ví dụ
my_list = [1, 2]
printPairs(my_list)
