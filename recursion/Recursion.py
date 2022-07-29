def countDown(n):
    print(n)

    if n == 0:
        return
    else:
        countDown(n-1)


def sum(list):
  if list == []:
     return 0
  return list[0] + sum(list[1:])


def countIndex(list):
    if list == []:
        return 0
    return 1 + countIndex(list[1:])


def max(array):
    if len(array) == 2:
        if array[0] > array[1]:
            return array[0]
        else:
            return array[1]
    sub_max = max(array[1:])
    if array[0] > sub_max:
        return array[0]
    else:
        return sub_max


print(sum([]))
print(countIndex([1, 23, 3]))
print(max([1, 23, 3]))


def quicksort(array):
 if len(array) < 2:
  return array
 else:
  pivot = array[0]
  less = [i for i in array[1:] if i <= pivot]
  greater = [i for i in array[1:] if i > pivot]
  return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
