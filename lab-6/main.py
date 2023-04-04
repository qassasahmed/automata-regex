#the x flag
#the m flag
#backrefrences
import re


def validate_email(txt):
    email_pattern = re.compile(r'^([\w.]+)@([\w.]+)\.([a-z.]{2,4})$', re.I)
    email_pattern_x = re.compile(r"""
    ^([\w.]+)         #start with username
    @                 #literal @
    ([\w.]+)          #domain name
    \.                #literal dot
    ([a-z.]{2,4})$    #ends with top level domain
    """, re.X | re.I)
    return email_pattern_x.fullmatch(txt)


if __name__ == '__main__':
    e = validate_email('qassas.ahmed@mau.edu.eg')
    if(e):
        print(f'email: {e.group(0)}')
        print(f'hostname: {e.group(1)}')
        print(f'domain name: {e.group(2)}')
        print(f'top level domain: {e.group(3)}')
        print(f'all: {e.group(1,2, 3)}')
    else: 
        print('None: no match object')

