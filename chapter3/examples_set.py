
vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
print(vowels)

vowels2 = set('aeeiouu')
print(vowels2)


vowels = set('aieuo')
word = 'hellow'
u = vowels.union(set(word))
print(u)

u_list = sorted(list(u))
print(u_list)

d = vowels.difference(set(word))
print(d)

i = vowels.intersection(set(word))
print(i)
