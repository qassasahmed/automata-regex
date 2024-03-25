import re

#Here we used the * meta character
pattern_star = re.compile('ab*c')
print(re.fullmatch(pattern_star, "abbbc"))
print(re.fullmatch(pattern_star, "ac"))

# Here we used the + meta character
pattern_plus = re.compile('ab+c')
print(re.fullmatch(pattern_plus, "abbbc"))
print(re.fullmatch(pattern_plus, "ac"))