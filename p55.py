#write a pp to perform searching activity using linear and binary search
# Program to perform Linear Search and Binary Search

arr = list(map(int, input("Enter elements separated by space: ").split()))

key = int(input("Enter element to search: "))

print("\n1. Linear Search")
print("2. Binary Search")

choice = int(input("Enter your choice: "))

# Linear Search
if choice == 1:
    found = False

    for i in range(len(arr)):
        if arr[i] == key:
            print("Element found at position", i + 1)
            found = True
            break

    if not found:
        print("Element not found")


# Binary Search
elif choice == 2:
    # Binary search requires sorted array
    arr.sort()

    low = 0
    high = len(arr) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            print("Element found at position", mid + 1)
            found = True
            break

        elif key < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    if not found:
        print("Element not found")

else:
    print("Invalid choice")
