narysearch(values, key, left, right):
    middle = (left + right) // 2
    if values[middle] == key:
        return middle
    if left > right:
        return -1
    elif values[middle] > key:
        right = middle - 1
        return binarysearch(values, key, left, right)
    elif values[middle] < key:
        left = middle + 1
        return binarysearch(values, key, left, right)


values = [2, 6,8,12,14,34,45,67,76,77,88,89,91,96,105]
key = int(input('input your num:'))
left = 0
right = len(values) - 1
result = binarysearch(values,key,left, right)

print(result)

