# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        l = merge_sort(arr[0: len(arr) // 2])
        r = merge_sort(arr[len(arr) // 2:])
        arr = merge(l, r)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    middle = mid
    arrA = merge_sort(arr[:middle])
    arrB = merge_sort(arr[middle:])
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            arr[k] = arrA[i]
            i += 1
            k += 1
        else:
            arr[k] = arrB[j]
            j += 1
            k += 1

    remaining = arrA if i < j else arrB
    r = i if remaining == arrA else j

    while r < len(remaining):
        arr[k] = remaining[r]
        r += 1
        k += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    result = []
    if len(arr) == 0:
        return result
    elif len(arr) == 1:
        return arr
    else:
        return merge_in_place(arr, l, int(len(arr)/2), (r + 1))
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
