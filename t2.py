import locale


def fopen(fpath, fmode = 'r'):
    f = open('C:/Users/bodnj/Desktop/univ/lab4/' + fpath, 'r')
    data = f.read()
    f.close()
    return data


def bigram(fpath, data):
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    bigrams = {}
    data_without_spaces = ''.join(char for char in data if not char.isspace())
    data_lowercase = data_without_spaces.lower()
    for i in range(len(data_lowercase) - 1):
        bigram = (data_lowercase[i], data_lowercase[i + 1])
        if all(char.isalpha() for char in bigram):
            bigrams[bigram] = bigrams.get(bigram, 0) + 1

    sorted_bigrams = dict(sorted(bigrams.items(), key=lambda item: item[1], reverse=True))

    print('\nбіграма\t\tвідносна частота')
    i = 0
    for key, value in sorted_bigrams.items():
        i = i + 1
        print(key[0] + key[1] + '\t\t' + round(value / (len(data) - 1), 5).__str__() + '\t\t')
    print('total count: ' + i.__str__())


#bigram('2.txt', fopen('2.txt'))
bigram('2.txt', fopen('2.txt'))
print('\n')