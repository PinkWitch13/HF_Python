
def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

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
