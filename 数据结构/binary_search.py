"""二分查找
二分查找算法的时间复杂度为O(log n)
"""
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 13, 34, 45]

print(binary_search(my_list, 20))
