# Problem: Two Number Sum
def two_num_sum_brute_force(array, target_sum):
    for i in range(len(array)): # to access indices from 0
        for j in range(i + 1, len(array)): # to access indices from 1
            if array[i] + array[j] == target_sum:
                # you access each number with array[i]
                return [array[i], array[j]]
    return [] #return an empty list if not pair is found

def two_num_sum_hash_table(array, target_sum):
    hash_table = {}  # dictionary because each element (num) must be unique
    for num in array:
        potential_match = target_sum - num 
        if potential_match in hash_table:
            return [potential_match, num]
        else:
            hash_table[num] = True # Mark this number as "seen"
    return []
