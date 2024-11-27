def alphanumericseperation(str):
    number = ''
    alphabets = ''
    special_characters = ''
    for x in str:
        if x.isalpha():
            alphabets += x
        elif x.isnumeric():
            number += x
        else:
            special_characters += x
              
    print("Numeric values:", number + " Alphabates:", alphabets + " special characters:", special_characters)

str = "dha#na2la3kshmi4"
alphanumericseperation(str)
# a = str.isdigit()
# b = str.isalpha()
# # print(a, b)
# for x in str:
#     if type(x) == a:
#         print(a)
#     else:
#         print(b)

"""
# str = list(a)
str = ["a", 2, "b", 4]
for x in str:
    if type(x) == int:
        continue
    print(x, type(x))

"""

# input: abc#d
# output: abd    




  