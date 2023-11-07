unsorted = [1, 6, 2, 11, 3, 2]

def selection_sort(arr: list) -> list:
    sorted_list = []
    arr_copy = arr[:]
    while len(arr_copy):
        minim = arr_copy[0]
        minim_index = 0
        for i, n in enumerate(arr_copy):
            if n < minim:
                minim = n
                minim_index = i
        sorted_list.append(minim)
        arr_copy.pop(minim_index)
    return sorted_list

print('input: ', unsorted, 'result: ', selection_sort(unsorted))