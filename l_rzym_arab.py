liczby_arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
liczby_rzym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

def zapis_rzymski(number):
    zapis_rzym = ""
    while number > 0:
        if number >= liczby_arab[0]:
            number = number - liczby_arab[0]
            zapis_rzym = zapis_rzym + liczby_rzym[0]
        elif number >= liczby_arab[1]:
            number = number - liczby_arab[1]
            zapis_rzym = zapis_rzym + liczby_rzym[1]
        elif number >= liczby_arab[2]:
            number = number - liczby_arab[2]
            zapis_rzym = zapis_rzym + liczby_rzym[2]
        elif number >= liczby_arab[3]:
            number = number - liczby_arab[3]
            zapis_rzym = zapis_rzym + liczby_rzym[3]
        elif number >= liczby_arab[4]:
            number = number - liczby_arab[4]
            zapis_rzym = zapis_rzym + liczby_rzym[4]
        elif number >= liczby_arab[5]:
            number = number - liczby_arab[5]
            zapis_rzym = zapis_rzym + liczby_rzym[5]
        elif number >= liczby_arab[6]:
            number = number - liczby_arab[6]
            zapis_rzym = zapis_rzym + liczby_rzym[6]
        elif number >= liczby_arab[7]:
            number = number - liczby_arab[7]
            zapis_rzym = zapis_rzym + liczby_rzym[7]
        elif number >= liczby_arab[8]:
            number = number - liczby_arab[8]
            zapis_rzym = zapis_rzym + liczby_rzym[8]
        elif number >= liczby_arab[9]:
            number = number - liczby_arab[9]
            zapis_rzym = zapis_rzym + liczby_rzym[9]
        elif number >= liczby_arab[10]:
            number = number - liczby_arab[10]
            zapis_rzym = zapis_rzym + liczby_rzym[10]
        elif number >= liczby_arab[11]:
            number = number - liczby_arab[11]
            zapis_rzym = zapis_rzym + liczby_rzym[11]
        else:
            number = number - liczby_arab[12]
            zapis_rzym = zapis_rzym + liczby_rzym[12]

    return zapis_rzym


def zapis_arabski(number):
    zapis_rzym = number.upper()
    l_arab = 0
    l = 0

    for i in range(len(liczby_rzym)):
        while zapis_rzym.startswith(liczby_rzym[i], l):
            l_arab = l_arab + liczby_arab[i]
            l = l + len(liczby_rzym[i])
    return l_arab

ar = input("Podaj liczbę w systemie arabskim: ")
print(zapis_rzymski(int(ar)))
rz = input("Podaj liczbę w systemie rzymskim: ")
print(zapis_arabski(rz))
