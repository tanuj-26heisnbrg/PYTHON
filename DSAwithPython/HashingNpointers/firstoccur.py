# Question 2: First Repeating Element

# Given:

# arr = [4, 7, 2, 7, 9, 4, 2]

# Using hashing, find the first element that appears more than once.

# Expected output:

# 7


def first_repeat(lst):
    """Return the first element that appears more than once in a list."""

    res = None
    d = dict()
    for ele in lst:
        if ele in d:
            res = ele
            break
        else:
            d[ele] = True

    return res





OUR_LIST = [4, 7, 2, 7, 9, 4, 2]

result = first_repeat(OUR_LIST)

print(result)





# flow understanding :

# Check whether we've seen the element
# if ele in d:

# This asks:

# Is ele already present in our dictionary?

# For the first element:

# ele = 4
# d = {}

# 4 isn't there, so the condition is False.

# Now, Store new elements
# else:
#     d[ele] = True

# For 4:

# d[4] = True

# Now:

# d = {4: True}

# Then 7:

# d = {
#     4: True,
#     7: True
# }

# Then 2:

# d = {
#     4: True,
#     7: True,
#     2: True
# }

# The actual value True isn't particularly important.

# You're basically saying:

# 4 → seen
# 7 → seen
# 2 → seen
# 7. We encounter 7 again

# Eventually:

# ele = 7

# But the dictionary already contains 7.

# Therefore:

# if ele in d:

# is True.

# So:

# res = ele

# becomes:

# res = 7
# 8. Stop immediately
# break

# This is important.

# It stops the loop immediately.

# So you don't continue checking:

# 9
# 4
# 2

# because you've already found the first repeated element.