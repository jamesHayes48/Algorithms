def sliding_max_subarray(arr, k):
    '''
    Used to find max subarray with a sliding window.

    Kadane's Algorithm
    :param arr:
    :param k:
    :return:
    '''
    window_sum = 0
    max_result = -1
    n = len(arr)

    # Calculate first sum of the window size k
    for i in range(0, k):
        window_sum += arr[i]

    # Initialize max sum
    max_result = window_sum

    # slide window
    for i in range(k, n):
        # Update window sum by subtracting element leaving the window from the left
        # Add new element entering from the right
        window_sum += arr[i] - arr[i - k]
        max_result = max(max_result, window_sum)
    return max_result

def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            # if character in set, shrink window
            char_set.remove(s[left])
            left += 1

        # Add current character in the set and update max length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

my_array = [-1, 2, 5, -7, 6, 8, 7, -100]
print(sliding_max_subarray(my_array, 3))
