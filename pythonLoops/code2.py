# loops with  python  lists

# question: You are given an array arr of size n - 1 that contains distinct integers
# in the range from 1 to n (inclusive). This array represents a permutation of the integers
# from 1 to n with one element missing.
#  Your task is to identify and return the missing element.


nums = [1, 2, 3, 5]
# method 1 :

nums.sort()

for i in range( 1 ,len(nums)):
    if(nums[i-1] + 1 != nums[i]):
        print(f"the  missing number is : {nums[i-1] + 1}")
        break
    else :
        continue



# method 2 

sum = 0
m =-1
for a in  nums:
    m = max(a , m)
    sum  = sum + a

n =  len(nums)
print(n)
totalsum = 0

for b  in range(0, m+1):
    totalsum =totalsum + b

ans =  totalsum - sum
print(f"missing  numbser from the array is : {ans}")

