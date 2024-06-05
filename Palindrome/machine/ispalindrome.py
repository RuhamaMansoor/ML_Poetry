def ispalindrome(s):
    # Convert to lower case and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Example usage
Palindrome_input_Variable = ['AnnA', 'SoloS', 'RotatoR', 'RadaR', 'SagaS', 'RotoR', 'TenT', 
                             'RepapeR', 'CiviC', 'KayaK', 'Lever', 'MadaM', 'RacecaR', 'StatS', 
                             'Redder', 'Wow', 'MoM', 'RefeR', 'NooN']

print("PALINDROME CHECK PROGRAM")
for i in Palindrome_input_Variable:
    ans = ispalindrome(i)
    if ans:
        print("The given string", "'", i, "'", "is a palindrome")
    else:
        print("The given string", "'", i, "'", "is not a palindrome")
