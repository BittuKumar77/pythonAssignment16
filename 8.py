# 8. Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

t1=(('a',23),('b',37),('c',11),('d',29))
t1=tuple(sorted(list(t1),key=lambda x:x[1]))
print(t1)