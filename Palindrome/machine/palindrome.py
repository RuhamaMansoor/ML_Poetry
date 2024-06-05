# TEST 1 WITH STRINGS :

def palindrome(var:str):
    
    if var == var[::-1]:
        return True
    else:
        return False
    
print(palindrome("deed"))


    