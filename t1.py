import math
import locale

def fopen(fpath, fmode = 'r'):
    f = open('C:/Users/bodnj/Desktop/univ/lab4/' + fpath, 'r')
    data = f.read().lower()
    f.close()
    return data


def count(fpath, data):
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    # частота символів
    charfreq = {}
    for char in data:
        if char.isalnum() or char.isspace() and char not in ['\t', '\n']:
            if char in charfreq:
                charfreq[char] += 1
            else:
                charfreq[char] = 1

    sorted_charfreq = dict(sorted((key.lower(), value) for key, value in charfreq.items()))



    print('Файл ' + fpath + ' - частота появи символів\n')
    print('символ\tвідносна частота')
    i = 0
    for key, value in charfreq.items():
        i = i + 1
        print(key + '\t\t' + round(value / len(data), 5).__str__() + '\t\t')



count('2.txt', fopen('2.txt'))
#('texty_gurgu.txt', fopen('texty_gurgu.txt'))
# count('text_gm.txt', fopen('text_gm.txt'))
print('\n')