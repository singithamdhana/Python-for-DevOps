#different datatypes in python
a = "python"  #str
b = 10  #int
c = 19.7 #float
d = 9j #complex
e = ["apple", "banana"] #list
f = ("apple", "banana") #tuple
g = range(5) #range
h = {"name" : "python", "type": "programming"} #dictonary
i = {"apple", "banana"} #set
j = frozenset({"apple", "banana", "cherry"}) #frozenset
k = True #bollean
l = b"Hello" #bytes
m = bytearray(5)	#bytearray
n = memoryview(bytes(5)) #memoryview
o = None #NoneType

#print type of value and type of data
print(a, type(a)) 
print(b, type(b)) 
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))  
print(k, type(k))  
print(l, type(l))  
print(m, type(m))  
print(n, type(n))
print(o, type(o))    

x = list(("hyderabad", "chennai", "bangulore"))
print (x, type(x))

#list example
p = ["Hyd", "delhi", "bombay"]
print("list of places are : ", p)
print("length of the list : ", len(p))
Q=[1,2,2]
print(Q)
R = [True, False]
print(R)
S = (('a','b')) #list() constructor 
print(S)