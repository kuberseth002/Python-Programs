# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
# Input: [0,1,0,3,12]
# Output: [1, 3, 12, 0, 0]

# Input: [1,7,0,0,8,0,10,12,0,4]
# Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]


def move_zero(num):
    zero_idx=0
    
    for i in range(len(num)):
        if num[i]!=0:
            num[zero_idx],num[i]=num[i],num[zero_idx]
            zero_idx += 1
            
arr1=[0,1,0,3,12]
move_zero(arr1)
print(arr1)

arr2=[1,7,0,0,8,0,10,12,0,4]
move_zero(arr2)
print(arr2)


# Q2

def swap_idx(arr):
    for i in range(0, len(arr) - 2, 4): 
        arr[i], arr[i+2] = arr[i+2], arr[i]
        arr[i+1], arr[i+3] = arr[i+3], arr[i+1]

arr = [2, 5, 11, 30, 7, 15, 9, 4, 3, 18] 
swap_idx(arr)
print(arr)