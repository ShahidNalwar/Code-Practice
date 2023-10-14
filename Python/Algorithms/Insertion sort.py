def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

array = input("Enter elements of the array separated by spaces: ")
arr = [int(x) for x in array.split()]
insertion_sort(arr)
print("Sorted array:", arr)
