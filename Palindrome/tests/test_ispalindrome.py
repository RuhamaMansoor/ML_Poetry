from machine.ispalindrome import ispalindrome

def test_is_palindrome():
    palindromes = ['AnnA', 'SoloS', 'RotatoR', 'RadaR', 'SagaS', 'RotoR', 
                   'RepapeR', 'CiviC', 'KayaK', 'MadaM', 'RacecaR', 'StatS', 
                   'Redder', 'Wow', 'MoM', 'RefeR', 'NooN']
    for word in palindromes:
        assert ispalindrome(word) == True

    non_palindromes = ['apple', 'banana', 'carrot', 'date', 'elephant']
    for word in non_palindromes:
        assert ispalindrome(word) == False

def test_is_palindrome_with_spaces():
    assert ispalindrome('race car') == True
    assert ispalindrome('a man a plan a canal panama') == True

def test_is_palindrome_with_punctuation():
    assert ispalindrome("madam, I'm Adam") == True
