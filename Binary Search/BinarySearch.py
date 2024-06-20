def binary_search(arr, target):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter the sorted array elements separated by space: ").split()))
    
    target = int(input("Enter the target element to search for: "))
    
    index = binary_search(arr, target)
    
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in the array.")
