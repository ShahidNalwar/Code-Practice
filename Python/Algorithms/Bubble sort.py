def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input from the user
input_str = input("Enter elements of the array separated by spaces: ")
arr = [int(x) for x in input_str.split()]

bubble_sort(arr)

print("Sorted array:", arr)
