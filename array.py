# Sort an Array (Without Built-in Sort)

# Input:
# [5, 2, 8, 1, 3]

# Output:
# [1, 2, 3, 5, 8]

#      0,1,2,3,4 = i
arr = [5,2,8,1,3]
#      j= i+1

for i in range(len(arr)):

    for j in range(i+1,(len(arr))):

        if arr[i]>arr[j]:

            arr[i],arr[j] = arr[j],arr[i]

print(arr)