def sogl(s):
    c = 0
    for i in range(len(s)+1):
        if s[i-1] == 'б' or s[i-1] == 'в' or s[i-1] == 'г' or s[i-1] == 'д' or s[i-1] == 'ж' or s[i-1] == 'з' or s[i-1] == 'й' or s[i-1] == 'к' or s[i-1] == 'л' or s[i-1] == 'м' or s[i-1] == 'н' or s[i-1] == 'п' or s[i-1] == 'р' or s[i-1] == 'с' or s[i-1] == 'т' or s[i-1] == 'ф' or s[i-1] == 'х' or s[i-1] == 'ц' or s[i-1] == 'ч' or s[i-1] == 'ш' or s[i-1] == 'щ':
            c += 1
    return c
def glas(g):
    c=0
    for i in range(len(g)+1):
        if g[i-1] == 'a' or g[i-1] == 'у' or g[i-1] == 'о' or g[i-1] == 'ы' or g[i-1] == 'э' or g[i-1] == 'я' or g[i-1] == 'ю' or g[i-1] == 'ё' or g[i-1] == 'е' or g[i-1] == 'и':
            c += 1
    return c
inp = str(input("Введите строку используя только строчные и русские буквы "))
choice = str(input("Что подсчитать? Гласные или согласные?"))
if choice == "Согласные" or "согласные":
    print(sogl(inp))
elif choice == "Гласные" or "гласные":
   print(glas(inp))

