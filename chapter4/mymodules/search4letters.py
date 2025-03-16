#vowels final version:
def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(f"The word is: {search4vowels('kotusia')}")
print(f"The word is: {search4vowels('sky')}")

#version 1.0:
def search4letters(phrase: str, letters: str) -> set:
    """Return s set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

print(f"same letters are: {search4letters('kotusia', 'lusia')}")

#version 2.0:
def search4letters(phrase: str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

print(search4letters('life, the universe, and everything'))
print(search4letters('life, the universe, and everything', 'aeiou'))
