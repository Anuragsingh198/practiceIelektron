'''Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j 
and arr[i] + arr[j] == 0.'''

nums = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]


nums.sort()

i =0
n = len(nums)
j = n-1

while i<j:
    sum =  nums[i]  + nums[j]
    if( sum == 0) :
        print(f"pair with the  sum 0 is : {nums[i] , nums[j]}")
        i = i+1
        j= j-1
    elif( sum > 0):
        j= j-1
    else:
        i = i+1


