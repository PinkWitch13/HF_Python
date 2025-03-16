
def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(f"The word is: {search4vowels('kotusia')}")
print(f"The word is: {search4vowels('sky')}")

# long_list = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7
# ]

# long_str = (
#             "beginnnnnnnnnnnnnnn"
#             "nnnnnnnnnnn"
#             "nnnnnnning"
# )
