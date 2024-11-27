a = "hello"
b = 'hii'
c = "I'm learning Python"
d = "Python is 'simple' programming language"
e = 'It is similar like "English"'
f = """ The uses of python is
    we can use it in web development
    software development
    For big data file read and modify
    For mathematics as well
    """
print(a,b,c,d,e,f)
print(a[1]) #array of string
print(len(a)) #length of the string
print('the' in d) #character present or not

#if character is present then only print the statement
if 'simple' in d:
    print("yes, it's present")
else:
    print("No, It's not present")

print('the' not in d) #the character not present say true

#print only when character is not present
if "simple" not in d:
    print("yes, It's not present")
else:
    print("No, It's present")

#slicing string
print("printing 2 to 5 character : " + a[2:5])  #print 2 to 5(not included) charcters
print("slicing from starting to 5 : " + a[:5])# slicing from start
print("slicing from end to 4 : " + a[1:]) #slicing from end
print(a[-4:-1]) # negative indexing

#Modifying string
M = " Hii, I'am Working on String Modifications " 
N = "let's start working on it"
print("Statement in upper case : " + M.upper())#change text to Upper
print("statemenr in lower case :" +M.lower())#change text to lower
print(M.split(","))#Split the text a.split(",")
print("Replace the word : " + M.replace("Modifications" , "replace"))#replace the characters
print("Removing whitespaces form beginning and ending : " + M.strip())#remove whitespaces
print("cancatinate two string : " + (M+N))

#combining string and number by using f-string

O = 20
P = f"Total students present in class : {O}"
print(P)

Q = "hello,\nGood morning"
print(Q)