# input: abc#d
# output: abd 
def remove_before_hash(str):
    if "#" in str:
        return str.split("#", 1)[1]
    else:
        return str    
str = "abc#d"
remove_before_hash(str)