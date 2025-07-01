def is_pangram(st):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    found = set(st)
    if alphabet.issubset(found):
        return True
    else:
        return False
print(is_pangram)