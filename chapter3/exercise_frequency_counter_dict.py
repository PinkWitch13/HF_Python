found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

found['e'] = found['e'] + 1
found['e'] += 1
print(found)

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

