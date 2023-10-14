pos = -1

def Binary_search(list, n):
    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lower = mid + 1  
            else:
                upper = mid - 1  
    return False 

array = input("Enter elements of the array separated by spaces: ")
arr = [int(x) for x in array.split()]

n = int(input("Enter the number to be searched: "))  

if Binary_search(arr, n):
    print(f"Element {n} found at position {pos}.")
else:
    print(f"Element {n} not found in the array.")
