import re


def email(e):
    return True if re.fullmatch(r"[^@/-]+@[^@]+\.[^@]+", e) else False


def password(p):
    return True if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", p) else False


def domain_name(d):
    return True if re.fullmatch(r"[a-z0-9]+([\-.][a-z0-9]+)*\.[a-z]{2,5}", d) else False


if __name__ == "__main__":
    print('navigate to main.py to run the program')
