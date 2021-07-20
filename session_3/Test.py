my_list = [1, 2, 3]
p = lambda x: x+1
result = map(p, my_list)
# builds something like [p(1), p(2), p(3)]
p = lambda x: x+2
print([*result])
