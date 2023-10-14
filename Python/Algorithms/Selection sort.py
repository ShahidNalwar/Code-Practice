def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Input from the user
input_str = input("Enter elements of the array separated by spaces: ")
arr = [int(x) for x in input_str.split()]

selection_sort(arr)

print("Sorted array:", arr)
