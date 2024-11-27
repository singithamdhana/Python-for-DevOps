# print integer values
a = 20
b = -20
c = 0
print (a,b,c, type(a),type(b), type(c))

# print float values
d = 10.56
e = -56.76
f = -0.0000
print(d,e,f, type(d), type(e), type(f))

#complex numbers
g = 3+5j
h = 5j
i = -5j
print(g, h, i, type(g), type(h), type(i))

# Type conversions
j = 20
k = 29.67
l = 30+6j

m = float(j)
n = int(k)
l = complex(j)

print(m,n,l)

#print random number using random module 
import random
print (random.randrange(100))



