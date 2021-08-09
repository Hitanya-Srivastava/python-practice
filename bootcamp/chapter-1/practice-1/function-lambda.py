# Code to illustrate cube of a number
# Difference between def() and lambda().

def cube(y) :
    return y*y*y

lambda_cube = lambda y: y*y*y

# defined function

print(cube(7))

# lambda function

print(lambda_cube(7))

# filter() with lambda()

li = [5, 7, 67, 86, 78, 89, 45, 56, 98]
final_list = list(filter(lambda x: (x*2 != 0) , li))
 print(final_list)

 # map() with lambda()

 li = [5, 7, 43, 67, 77, 56, 23, 61, 67, 56]

 final_list = list(map(lambda x: x*2, li))
 print(final_list)

 # reduce() with lambda()

 from functools import reduce
 li = [5, 6, 7, 8, 10, 11, 100]
 sum = reduce((lambda x, y: x + y), li)
 print(sum)
