empty_tuple = tuple()  # show __builtin__
tuple1 = (1, )
tuple2 = (1, )
not_a_tuple = (1)  # this is not a tuple!

print(tuple1 == tuple2, tuple2 == not_a_tuple, type(not_a_tuple), not_a_tuple)
print( (1, 2) == (1, 2, ) )