tuple_int = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
convert = list(tuple_int)
convert[9] = 22
tuple_int = tuple(convert)
for i in tuple_int:
    print(tuple_int)
