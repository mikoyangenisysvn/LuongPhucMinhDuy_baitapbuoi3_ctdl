def printUnorderedPairs(lstA, lstB):
    for a in lstA:
        for b in lstB:
            if a < b:
                print(f"{a},{b}")

# Sử dụng hàm với các danh sách ví dụ
listA = [1, 3, 5]
listB = [2, 4, 6]
printUnorderedPairs(listA, listB)
