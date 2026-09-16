arr = [-8, 1, 4, 6, 10, 12]
target = 16
n = len(arr)
left = 0 
right = n-1 


paircount = []

while left < right:
 sum = arr[left] + arr[right]

 if sum == target:
          paircount.append(sum)
          left += 1 
          right -=1 
 elif sum < target:
          left +=1 
 else:
     right -= 1

print (arr)
   












# arr = [-1, 2, 2, 1, -1]
# n = len(arr)
  
# i = 0
# while i< n :
#        if arr[i] != -1 and arr[i] != i and arr[i]<n :
#          x = arr[i]

#          if arr[x] != x:
#               arr[i],arr[x] = arr[x],arr[i]

#          else :
#               arr[i]=-1
#               i+=1
#        else:
#           i+=1            

# print(arr)
    # n = len(arr)
    # result =[-1]*n 

    # for num in arr :
    #      if 0 <= num <n :
    #           result[num] = num

    # return result

# answer = calculate(arr)

