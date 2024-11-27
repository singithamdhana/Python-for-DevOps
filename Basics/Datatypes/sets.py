# joining sets
set1 = {"1", "2"}
set2 = {"3", "4"}
set3 = set1.union(set2)
set4 = set1 | set2 #it will wrok as union
print(set3, set4)
set5 = set1.union(set2, set3, set4)
print(set5)

# intersection (only print dublication)
a = {'1', '2', '3'}
b = {'2', '3', '4'}
c = a.intersection(b)
print(c)
d = a & b # similar like intesection
print(d)

# difference items
e = a.difference(b)
print(e)
f = a - b # similar like difference
print(f)
