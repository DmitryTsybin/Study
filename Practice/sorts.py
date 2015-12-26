def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[len(array) / 2]

    lt = [ x for x in array if x < pivot ]
    ge = [ x for x in array if x > pivot ]
    eq = [ x for x in array if x == pivot ]
    return quicksort(lt) + eq + quicksort(ge)


def quicksort0(array):
    if len(array) < 2:
        return array

    pivot = array[0]

    lt = [ x for x in array[1:] if x < pivot ]
    ge = [ x for x in array[1:] if x >= pivot ]

    return quicksort0(lt) + [pivot] + quicksort0(ge)


def merge(left, right):
    result = []
    i = 0
    j = 0

    if len(left) == 0:
        return right[:]

    if len(right) == 0:
        return left[:]

    if left[0] < right[0]:
        result.append(left[0])
        i += 1
    else:
        result.append(right[0])
        j += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        result += right[j:]
    elif j == len(right):
        result += left[i:]

    return result


def merge_func(left, right):
    def merge_(acc, left, right):
        if len(left) == 0:
            return acc + right

        if len(right) == 0:
            return acc + left

        if left[0] < right[0]:
            return merge_(acc + [left[0]], left[1:], right)
        else:
            return merge_(acc + [right[0]], left, right[1:])

    return merge_([], left, right)


def mergesort(array, mergefunc=merge):
    if len(array) < 2:
        return array

    left = mergesort(array[:len(array) / 2])
    right = mergesort(array[len(array) / 2:])

    return mergefunc(left, right)


test_arr_1 = [1, 3, 3, 3, 5, 7, 5, 9, 0, 8, 7, 6, 4, 2]
#print quicksort0(test_arr_1)
#print mergesort(test_arr_1)
#print mergesort(test_arr_1, merge_func)

print medresort([random(x) for x in ])

#print merge([1,3], [2, 4])
