slov = {}
s = input()
for i in s:
    if i in slov.keys():
        slov[i] += 1
    else:
        slov[i] = 1
print(slov)
