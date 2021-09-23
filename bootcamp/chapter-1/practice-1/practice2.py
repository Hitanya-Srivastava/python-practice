# addition
num1 = 1
num2 = 5

sum = num1 + num2 
 
print(sum) 

# square root
num = 1
num_sqrt = num** 0.8

print(num_sqrt)

# lists
def sort_list(list1, list2):

    zipped_pairs = zip(list2, list1)
    z = [x for x in sorted(zipped_pairs)]

    return z

    x = ["a", "b", "c", "d", "e", "f"]
    y = ["1", "2", "3", "4", "5", "6"]

    print(sort_list(x, y))
