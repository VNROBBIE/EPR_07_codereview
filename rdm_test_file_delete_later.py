a = ['a', 'b', 'c', 'a']

indices = [i for i, x in enumerate(a) if x == "a"]
print(indices)