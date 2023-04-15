#1 lookahead and negeative lookahead
#2 lookbehind and negative lookbehind
##2.1 lookbehind limitations 
#3 named group
import re


#lookahead: (?=pattern)
pat1 = re.compile(r'hello(?=\s?world)')
m = pat1.search('hello world')
print(m)
#negative lookahead (?!pattern)
pat2 = re.compile(r'hello(?!\s?world)')
m2 = pat2.search('hello ahmed')
print(m2)


#lookbehind: (?<=pattern)
pat = r'(?<=welcome).+'
text = 'welcome ali'
m3 = re.search(pat, text)
print(m3)
#negative lookbehind: (?>!pattern)
#limitation: lookbehind requires fixed-width pattern
#lookahead and lookbehind are noncapturing groups, meaning you can't reference them
m4 = re.search(r'(?<!welcome).+', text)
print(m4) #welcome ali!


#named group: (?P<name>pattern)
text2 = 'blue blue xdelete thisx extre blue'
pat3 = re.compile(r'(?P<del>x).+?(?P=del)(?#\1 can be used too)', re.I)
#remember: * + and ? are greedy.
res = re.sub(pat3, repl='', string=text2 )
print(res)
#we can refer to a named group in three ways:
##a- \1
##b- \g<name>: used only with repl argument
##c- .group(name/number)


def spaceRemover(txt):
    """
    this function removes extra spaces from the given txt
    """
    return ' '


test = "the quick   brown fox jumps over the   lazy        dog"
result = re.sub(r'\s+', spaceRemover, test) 
print(result)
#expected output: the quick brown fox jumps over the lazy dog    







