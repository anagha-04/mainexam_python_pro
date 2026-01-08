# #find the missing number

arr =[1,2,4,5,6]

start = 1
end = 6

for i in range(start,end+1):

    if i not in arr:

        print(i)

# find the missing number from this array

array =[10,11,12,14,15]

start= 10
end = 15

for i in range(start,end+1):

    if i not in array:

        print(i)


arrays =[10,12,16,18]

diff = arrays[1] - arrays[0]# 4-2 = 2

for i in range(len(arrays)-1):

    if arrays[i+1] - arrays[i] != 2:

        missing = arrays[i] + diff

        print(missing)



ar = [1,3,5,9]

difference= ar[1] - ar[0]

for i in range(len(ar)-1):

    if ar[i+1]-ar[i]!=2:

        miss = ar[i]+difference

        print(miss)