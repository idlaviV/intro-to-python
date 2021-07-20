
#------------------------------------------------------------------------------#
# (1)
# Write a function which simulates the for loop without using any loop
# (printing out every value)
def fo(*args):	
    start = 0
    skip = 1
    if len(args) == 1:
        end = args[0]
    elif len(args) == 2:
        start = args[0]
        end = args[1]
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        skip = args[2]
    else:
        return "Wrong number of args provided"
    if start < end:	
        print(start)
        new_start = start + skip
        fo(new_start, end, skip)
        

fo(0, 10)
fo(10)
fo(1, 11, 2)


#------------------------------------------------------------------------------#
# (2)
# Write a function which simulates the for sum function

def ssum_1(*args):
    # support lists and single args
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    sum_value = 0
    for v in args:
        sum_value += v
    return sum_value

def ssum_2(*args):
    # support lists and single args
    if isinstance(args, tuple):
        args = list(args)
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    if not args:
        return 0 
    v = args.pop()
    return v + ssum_2(args)
    
print(ssum_2([1,2,3]))
print(ssum_2(1,2,3))
print(ssum_1([1,2,3]))
print(ssum_1(1,2,3))