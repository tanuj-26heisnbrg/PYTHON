# Question: Find the element with the highest frequency

# Given:

# arr = [1, 3, 2, 1, 4, 1, 3, 2, 3, 3]

# Write:

# def max_frequency(arr):
#     # your code

# Expected output:

# 3

# Because:

# 1 → 3 times
# 2 → 2 times
# 3 → 4 times  ← highest
# 4 → 1 time


def first_repeat(lst):
    """Return the highest frequency element that appears in a list."""

   
    d = dict()
    for ele in lst:
        if ele in d:
            d[ele] += 1
        
        else:
            d[ele] = 1

    return d





OUR_LIST =  [1, 3, 2, 1, 4, 1, 3, 2, 3, 3]

result = first_repeat(OUR_LIST)

highFreq = float('-inf')
highEle = None

for x in result :
   
    if result[x] > highFreq:
        highFreq = result[x]
        highEle = x

print(highEle, ":" , highFreq)