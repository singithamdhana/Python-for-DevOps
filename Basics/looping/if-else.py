a, b = 100, 200
#elif (if condition is true print, or check the else condition)
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")   
else:
    print("a is less than b")  
#shortest form    
print(">") if a > b else print("<") if a < b else print ("=") 