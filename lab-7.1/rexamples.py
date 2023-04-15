import re

# 1. Write a Python program to check that a string (contains only) a certain set of characters (in this case a-z, A-Z and 0-9).
def check_string1(string):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return 'valid' if pattern.match(string) else 'invalid'


# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
def check_string2(string):
    pattern = re.compile(r'^ab*$')
    return 'valid' if pattern.match(string) else 'invalid' 


# 3. Write a Python program that matches a string that has an a followed by one or more b's.
def check_string3(string):
    pattern = re.compile(r'^ab+$')
    return 'valid' if pattern.match(string) else 'invalid'


# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
def check_string4(string): 
    pattern = re.compile(r'^ab?$')
    return 'valid' if pattern.match(string) else 'invalid'


# 5. Write a Python program that matches a string that has an a followed by three 'b'.
def check_string5(string): 
    pattern = re.compile(r'^ab{3}$')
    return 'valid' if pattern.match(string) else 'invalid'


# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
def check_string6(string):
    pattern = re.compile(r'^ab{2,3}$')
    return 'valid' if pattern.match(string) else 'invalid'


# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
def check_string7(string):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    return 'valid' if pattern.match(string) else 'invalid'


# 8. Write a Python program to find sequences of one upper case letter followed by lower case letters.
def check_string8(string):
    pattern = re.compile(r'^[A-Z][a-z]+$')
    return 'valid' if pattern.match(string) else 'invalid'


# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def check_string9(string):
    pattern = re.compile(r'^a.*b$')
    return 'valid' if pattern.match(string) else 'invalid'


# 10. Write a Python program that matches a word at the beginning of a string.
def check_string10(string):
    pattern = re.compile(r'^\b\w+')
    return 'valid' if pattern.match(string) else 'invalid'


# 11. Write a Python program that matches a word at end of string, with optional punctuation.
def check_string11(string):
    pattern = re.compile(r'\w+\S*$')
    return 'valid' if pattern.match(string) else 'invalid'


# 12. Write a Python program that matches a word containing 'z'.
def check_string12(string):
    pattern = re.compile(r'\b\w*z\w*\b')
    return 'valid' if pattern.match(string) else 'invalid'


# 13. Write a Python program to match a string that contains only uppercase letters.
def check_string13(string):
    pattern = re.compile(r'^[A-Z]+$')
    return 'valid' if pattern.match(string) else 'invalid'


# 14. Write a Python program where a string will start with a specific number.
def check_string14(string):
    pattern = re.compile(r'^[1-9]')
    return 'valid' if pattern.match(string) else 'invalid'


# 15. Write a Python program to remove leading zeros from an IP address.
def remove_zeros15(string):
    pattern = re.compile(r'\b0+(\d+)')
    return pattern.sub(r'\1', string)


# 16. Write a Python program to check for a number at the end of a string.
def check_string16(string):
    pattern = re.compile(r'.*[0-9]$')
    return 'valid' if pattern.match(string) else 'invalid'


# 17. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
def check_string17(string):
    pattern = re.compile(r'([0-9]{1,3})')
    return pattern.findall(string)


# 18. Write a Python program to search some literals strings (any of three colors) in a string.
def check_string18(string):
    pattern = re.compile(r'(Red|White|Black)')
    return pattern.findall(string)


# 19. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
def check_string19(string):
    pattern = re.compile(r'(Red|White|Black)')
    return pattern.finditer(string)


# 20. Write a Python program to find the substrings within a string.
def check_string20(string):
    pattern = re.compile(r'w3resource')
    return pattern.findall(string)


# 21. Write a Python program to find the occurrence and position of the substrings within a string.
def check_string21(string):
    pattern = re.compile(r'w3resource')
    return pattern.finditer(string)


# 22. Write a Python program to do a case-insensitive string replacement.
def check_string22(string):
    pattern = re.compile(r'w3resource', re.IGNORECASE)
    return pattern.sub('Python', string)


# 23. Write a Python program to remove spaces from a given string.
def remove_spaces(string):
    pattern = re.compile(r'\s+')
    return pattern.sub('', string)


# 24. Write a Python program to remove everything (except alphanumeric) characters from a string.
def remove_chars(string):
    pattern = re.compile(r'\W+')
    return pattern.sub('', string)


# 25. Write a Python program to remove the characters which have odd index values (chars at even positions) of a given string.
## i.e., 'Python' -> 'Pto' or '123456789' -> '13579'
def remove_chars2(string):
    pattern = re.compile(r'(.)(.)')
    return pattern.sub(r'\1', string)


# 26. Write a Python program to return all the words the occurs twice  within a string.
def count_words(string):
    pattern = re.compile(r'(\w{2,})(?=\s.*\1)', re.I)
    return pattern.findall(string)


if __name__ == '__main__':
    print("rexamples.py: these functions aren't tested, but they should work.")







