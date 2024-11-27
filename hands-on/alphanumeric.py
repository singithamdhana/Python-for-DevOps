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
