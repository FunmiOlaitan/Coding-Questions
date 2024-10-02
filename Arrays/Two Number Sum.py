# Problem: Two Number Sum
def two_num_sum_brute_force(array, target_sum):
    for i in range(len(array)):  # Outer loop goes through all elements
        for j in range(i + 1, len(array)):  # Inner loop checks the rest
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []  # Return an empty list if no pair is found

def two_num_sum_hash_table(array, target_sum):
    hash_table = {}  # Using a dictionary for constant time lookups
    for num in array:
        potential_match = target_sum - num
        if potential_match in hash_table:
            return [potential_match, num]
        hash_table[num] = True  # Store the number in the dictionary
    return []  # Return an empty list if no pair is found

def two_num_sum_pointer(array, target_sum):
    sorted_array = sorted(array)  # Sort the array
    left = 0  # Left pointer starts at the beginning of the array
    right = len(sorted_array) - 1  # Right pointer starts at the end
    while left < right:
        current_sum = sorted_array[left] + sorted_array[right]
        if current_sum == target_sum:
            return [sorted_array[left], sorted_array[right]]
        elif current_sum < target_sum:
            left += 1  # Move the left pointer right to increase the sum
        else:
            right -= 1  # Move the right pointer left to decrease the sum
    return []  # Return an empty list if no pair is found


# Test array and target sum
array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10

# Testing all functions
print("Brute Force Method:", two_num_sum_brute_force(array, target_sum))
print("Hash Table Method:", two_num_sum_hash_table(array, target_sum))
print("Two Pointer Method:", two_num_sum_pointer(array, target_sum))