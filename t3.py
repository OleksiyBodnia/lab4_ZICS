import locale


def fopen(fpath, fmode = 'r'):
    f = open('C:/Users/bodnj/Desktop/univ/lab4/' + fpath, 'r')
    data = f.read()
    f.close()
    return data


def bigram(fpath, data):
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    trigrams = {}
    data_without_spaces = ''.join(char for char in data if not char.isspace())
    data_lowercase = data_without_spaces.lower()
    for i in range(len(data_lowercase) - 2):
        trigram = (data_lowercase[i], data_lowercase[i + 1], data_lowercase[i + 2])
        if all(char.isalnum() for char in trigram):
            trigrams[trigram] = trigrams.get(trigram, 0) + 1

    sorted_trigrams = dict(sorted(trigrams.items(), key=lambda item: item[1], reverse=True))

    print('\nтриграма\t\tвідносна частота')
    i = 0
    for key, value in sorted_trigrams.items():
        i = i + 1
        print(key[0] + key[1] + key[2] + '\t\t' + round(value / (len(data_lowercase) - 2), 5).__str__() + '\t\t')
    print('total count: ' + i.__str__())


bigram('2.txt', fopen('2.txt'))
# bigram('texty_gurgu.txt', fopen('texty_gurgu.txt'))
print('\n')