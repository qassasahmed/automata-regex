#lookahead
#lookbehind
#named group

import re


#lookahead (?=pattern)
pat1 = re.compile(r'hello(?=\s?world)')
m = pat1.search('hello world')
print(m)
#negative lookahead (?!pattern)
pat2 = re.compile(r'hello(?!\s?world)')
m2 = pat2.search('hello ahmed')
print(m2)

#lookbehind (?<=pattern)
pat = r'(?<=welcome).+'
text = 'welcome ali'
m3 = re.search(pat, text)
print(m3)
#negative lookbehind (?>!pattern)
#limitation: look-behind requires fixed-width pattern
#lookahead and lookbehind are noncapturing groups
m4 = re.search(r'(?<!welcome).+', text)
print(m4)


#named group: (?P<name>pattern)
text2 = 'blue blue xdelete thisx blue'
pat3 = re.compile(r'(?P<del>x).+(?P=del)(?#\1 can be used too)')
res = re.sub(pat3, repl='', string=text2 )
print(res)

#a- \1
#b \g<name>
#c .group(name/number)






