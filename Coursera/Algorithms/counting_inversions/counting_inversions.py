def readfile(path):
    '''Read integers from file to array'''
    array = []
    with open(path) as f:
        for line in f:
            array.append(int(line))
    return array


def mergesort(lst):
    '''Recursively divides list in halves to be sorted'''
    if len(lst) == 1:
        return lst, 0
    middle = len(lst)//2
    left, s1 = mergesort(lst[:middle])
    right, s2 = mergesort(lst[middle:])
    sortedlist, s3 = merge(left, right)
    return sortedlist, (s1+s2+s3)


def merge(left, right):
    '''Subroutine of mergesort to sort split lists.  Also returns number
    of split inversions (i.e., each occurence of a number from the sorted second
    half of the list appearing before a number from the sorted first half)'''
    i, j = 0, 0
    splits = 0
    result = []
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            splits += len(left[i:])
    result += left[i:]
    result += right[j:]
    # print(result, splits)
    return result, splits


print(mergesort(readfile('IntegerArray.txt')))


'''
print('Correct: 0; my: ', mergesort([1,2,3,4,5,6]))
print('Correct: 15; my: ', mergesort([6,5,4,3,2,1]))
print('Correct: 3; my: ', mergesort([1,3,5,2,4,6]))
print('Correct: 4; my: ', mergesort([1,5,3,2,4]))
print('Correct: 10; my: ', mergesort([5,4,3,2,1]))
print('Correct: 5; my: ', mergesort([1,6,3,2,4,5]))
print('Correct: 3; my: ', mergesort([3,2,1])) 
'''
