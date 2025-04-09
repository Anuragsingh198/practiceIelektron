# Given an array arr of integers, find all the elements that occur more than once in the array. 
# If no element repeats, return an empty array.

nums= [2, 3, 1, 2, 3]
from  collections  import Counter

count =  Counter(nums)

for key  , value in  count.items():
    if( value  > 1) :
         print (f" element which  occures more then  once is { key} ")
