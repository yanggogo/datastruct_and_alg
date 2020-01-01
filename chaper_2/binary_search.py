'''
二分查找算法


'''

def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

test_data = [
    ([1,2,3,4,5], 0, -1),
    ([1,2,3,4,5], 1, 0),
    ([1,2,3,4,5], 2, 1),
    ([1,2,3,4,5], 3, 2),
    ([1,2,3,4,5], 4, 3),
    ([1,2,3,4,5], 5, 4),
    ([1,2,3,4,5], 6, -1),
]

for arr, target, rslt in test_data:
    print(arr)
    print(target)
    assert binary_search(arr, target) == rslt

