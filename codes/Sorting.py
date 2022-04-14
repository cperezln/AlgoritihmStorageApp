#Mergesort
'''
    Autor: Admin
    Mergesort is a merging algorithm with complexity O(nlogn). It works with a "divide and conquer" approach.
    Works splitting the list into two sublist and ordering each one by "merging".
'''
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
#Quicksort
'''
    Autor: admin
    Quicksort is a sorting algorithm with complexity O(nlogn). It works with a "divide and conquer" approach.
    Works selecting a pivot element, and then dividing the list into two sublists, the left one which contains elements lower than the pivot, 
    and the right one with elements greater than the pivot.
'''
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)

