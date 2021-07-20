# ------------------------------------------------------------------------------#
# (1)
# Write a function which simulates the for loop without using any loop
# (printing out every value)
def loop(*args):
    if len(args) == 0:
        loop(10)
    elif len(args) == 1:
        inner_loop(0, args[0])
    elif len(args) == 2:
        inner_loop(args[0], args[1])
    else:
        inner_loop(args[0], args[1], args[2])


def inner_loop(lower, upper, step=1):
    i = lower
    print(i)
    i += step
    if i < upper:
        inner_loop(i, upper, step)


loop(10)
print("")
loop(1, 10)
print("")
loop(1, 10, 2)
print("")

# ------------------------------------------------------------------------------#
# (2)
# Write a function which simulates the for sum function

def my_sum(numbers, result=0):
    if len(numbers) == 0:
        return result
    else:
        return my_sum(numbers, numbers.pop())


arg = [1, 2, 3]
print(f"The sum of {arg} is {my_sum(arg)}.")
