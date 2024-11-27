#convert tuple to list and change value (because we can not change tuple value)
x = ("a", "b", "c")
y = list(x)
y[1] = "d"
x = tuple(y)
print(x)

#add tuple with tuple
a = ("1", "2")
b = ("3",)
c = a + b
print(c)
d = list(a)
a = d.remove("1")
print(d)
del a


#While loop in tuples
e = ("apple", "banana", "cherry")
i = 0
while i < len(e):
    print(e[i])
    i = i + 1



