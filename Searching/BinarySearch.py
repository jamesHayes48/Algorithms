
def binary_search(arr, item):
    '''
    Used to find item in a sorted array
    O(log(n))
    :param arr:
    :param item:
    :return:
    '''
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
