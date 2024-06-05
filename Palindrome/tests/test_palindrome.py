from machine.palindrome import palindrome

# Test with different stirngs and words
def test_palindrome_t1():
    assert palindrome("count") == False
    
def test_palindrome_t2():
    assert palindrome("deed") == True

def test_palindrome_t3():
    assert palindrome("civic") == True

