import re

str = 'blue ahmed96ma@google.com blue blue'
match = re.search(r'[\w.]+@[\w.]+', str)
print(f'{match.group()} was found' if match else 'no match')


def accept_language(string):
    language_pattern = re.fullmatch("(aa)*b+", string)
    return "accepted" if language_pattern else "not accepted"


if __name__ == '__main__':
    print(accept_language("aabb"))
