import rexamples

if __name__ == '__main__':
    # 1. Test a Python program to check that a string (contains only) a certain set of characters (in this case a-z, A-Z and 0-9).
    print(rexamples.check_string1('abcABC123')) # valid

    # 2. Test a Python program that matches a string that has an a followed by zero or more b's.
    print(rexamples.check_string2('aa')) # invalid

    # 3. Test a Python program that matches a string that has an a followed by one or more b's.
    print(rexamples.check_string3('aba')) # invalid

    # 4. Test a Python program that matches a string that has an a followed by zero or one 'b'.
    print(rexamples.check_string4('abb')) # invalid

    print(rexamples.remove_chars2('12345678'))
