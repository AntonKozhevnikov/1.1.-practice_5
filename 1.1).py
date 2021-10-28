a = [int(i) for i in input("Введите список: ").split()]
n = int(input("Введите число: "))
def inf (a = []):
    sp = []
    for i in range(0, len(a)):
        if a[i] > n:
            sp.append(a[i])
    return sp
print(inf(a))

    

