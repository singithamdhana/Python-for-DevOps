# method- 1 using max() function
a = input("first number : ")
b = input("second number: ")
print("maximum of two numbers is : ", max(a,b))

#method- 2 using condtional statements
if a > b:
    print ("a is greater value : ", a)
else:
    print ("b is greater", b)

# method-2 ternary operator
result = a if a > b else b
print(" the greater value is : ", result)