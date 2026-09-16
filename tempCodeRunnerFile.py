# This one tests whether you can use hashing without explicitly building a frequency table.

# Question: Two Sum

# Given:

# arr = [2, 7, 11, 15]
# target = 9

# Write:

# def two_sum(arr, target):
#     # your code

# Find the indices of the two elements whose sum equals target.

# Expected output:

# [0, 1]

# Because:

# arr[0] + arr[1]
#   2    +   7
#      = 9
# Constraints
# Use a dictionary/hash map
# Aim for O(n) average time
# Don't use nested loops
# Don't use index() repeatedly
# Hint

# As you traverse the array, for each element x, ask:

# What number do I need to reach target?

# That number is:

# target - x

# Then check whether you've already seen that number in your dictionary.

# This is one of the canonical hashing problems. If this clicks, a whole family of DSA questions starts looking suspiciously similar.


def twosum(lst , tar):
    newlst = list()
    for ele in lst:
        for ele2 in lst:
            if (ele + ele2) == target:
                newlst.append(ele)
                

    return newlst            
    



OUR_LIST = [2,7,11,15]
target = 9

result = twosum(OUR_LIST , target)

print(result)