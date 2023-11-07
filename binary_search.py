test_array = [x for x in range(10)]
# print(test_array)

def binary_search(arr: list, target: int) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] < target:
            low = mid + 1
    return False

# print('target: ', 5, 'result: ', binary_search(test_array, 5))
# print('target: ', 0, 'result: ', binary_search(test_array, 0))
# print('target: ', 9, 'result: ', binary_search(test_array, 9))
# print('target: ', 8, 'result: ', binary_search(test_array, 8))
# print('target: ', 10, 'result: ', binary_search(test_array, 10))
# print('target: ', 20, 'result: ', binary_search(test_array, 20))

edge_1 = [1,2]
print('target: ', '', 'result: ', binary_search(edge_1, 1))
print((7+8)//2)
