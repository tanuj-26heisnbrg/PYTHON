
nums = [7,2,3,90,3,9,4,4,5,89919] #list

unique = []

for no in nums:
    if no not in unique:
        unique.append(no)

numbers = [10, 5, 20, 8, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)
# 15        

print(unique)