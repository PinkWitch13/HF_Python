found = []
print(len(found))
found.append('a')
len(found)
found

found.append('e')
found.append('i')
found.append('o')
len(found)
found

if 'u' not in found:
    found.append('u')
print(found)

nums = [1, 2, 3, 4]
nums
nums.remove(3)
nums

nums.pop()
nums
nums.pop(0)
nums

nums.extend([3, 4])
nums.extend([])
print(nums)
