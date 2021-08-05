import re

def isValidPassportNo(number):
    regex = "^[A-PR-WYa-pr-wy][1-9]\\d" + "\\s?\\d{4}[1-9]$"
    p = re.compile(regex)
    if (number == ''):
        return False
    m = re.match(p, number)
    if m is None:
        return False
    else:
        return True


def isValidPanCardNo(number):
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
    regex1 = "[A-Z]{3}[0-9]{6}[A-Z]{1}"
    p = re.compile(regex)
    p1 = re.compile(regex1)
    if number == None:
        return False
    if re.search(p, number) or re.search(p1, number) and len(number) == 10:
        return True
    else:
        return False