# Count the total number of digits in a number


count =0
num = 123456789
while num  !=0:
    r = num%10
    count = count+ 1
    print(f"{r} ")
    num = num//10

print (f" the  count  of the  digits in the  given  number is : {count}")