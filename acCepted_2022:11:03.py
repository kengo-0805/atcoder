def isOK(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    if sum(map(str.isupper, s)) != 2:
        return False
    return True
print("AC" if isOK(input()) else "WA")