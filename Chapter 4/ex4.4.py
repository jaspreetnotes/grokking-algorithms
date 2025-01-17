# Remember binary search from chapter 1? It's a D&C Algorithm, too. Can
# you come up with the base case and the recursive case for binary search?

def binary_search(list, key):
    if (len(list) == 1 and list[0] != key) or list == []:
        return -1
    else:
        mid = len(list) // 2
        if key == list[mid]:
            return mid
        elif key < list[mid]:
            return binary_search(list[0:mid], key)
        elif key > list[mid]:
            return binary_search(list[mid+1:], key)
        return -1
    
items = [10, 20, 30, 40]  
key = 30  

index = binary_search(items, key)

if index == -1:
    print("Item not found.")
else:
    print(f"Item found.")