anums = list()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def is_coprime(a, b):
    return gcd(a, b) == 1


def encrypt(data, a, b):
    upper_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ '
    lower_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя '
    m = len(upper_alphabet)

    if not is_coprime(a, m):
        print("a is invalid")
        return

    buff = ''
    for char in data:
        if char in upper_alphabet:
            index = upper_alphabet.index(char)
            encrypted_index = (a * index + b) % m
            buff += upper_alphabet[encrypted_index]
        elif char in lower_alphabet:
            index = lower_alphabet.index(char)
            encrypted_index = (a * index + b) % m
            buff += lower_alphabet[encrypted_index]
        else:
            buff += char

    return buff


def decrypt(cipher_text, a, b):
    upper_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ '
    lower_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя '
    m = len(upper_alphabet)

    if not is_coprime(a, m):
        print("a is invalid")
        return
    anums.append(a)

    buff = ''
    a_inv = mod_inverse(a, m)
    for char in cipher_text:
        if char in upper_alphabet:
            index = upper_alphabet.index(char)
            decrypted_index = (a_inv * (index - b)) % m
            buff += upper_alphabet[decrypted_index]
        elif char in lower_alphabet:
            index = lower_alphabet.index(char)
            decrypted_index = (a_inv * (index - b)) % m
            buff += lower_alphabet[decrypted_index]
        else:
            buff += char

    return buff


def degen_brut(ciphertext):
    for a in range(1, 34):
        for b in range(34):
            decrypted_text = decrypt(ciphertext, a, b)
            print(f"a={a}, b={b}: {decrypted_text}")


text = "Стару попелясту гуску забив хворостиною в шкоді сусід і у варварській безсердечності прип'яв бездушного трупа за лапу до тієї ж хворостини, волік його так через ціле пасовисько"

a = 5
b = 16

encrypted = encrypt(text, a, b)
print('зашифровано:', encrypted)

sample = "Цфоґзґусхсг єизмкзими езоишьхтзе фмиїе оґєфгєияк ікяиььг є фсїзмщбпькук япмпзиьимиук"
# sample = "уйгтлчґьетґь чйчтчсґсєлвгсєґтеїуочґдчйє гвдйчґтчґсгвогйвщлчмчґдєич жґЛчйгґижогґвлефрхфеґвщчмчтфеґцхґкчдеочґнеохґдчйє гвдйчґйх дєдгґтчсейґає єаґвлч чґогухґьчґчиетеґ тч чмєґижоєґйь єйтеґфхґиогащлєґєохґсєлвгсґчиенбйґйгь чйєтгдгґдчйє гвдйчґь чвдеучяґоевчйчяґвдхюлчяґтчґджкоеґєґйетдєсґтчґтйч єґджмє єґйчйлєґ"

# degen_brut(encrypted)
# print(anums)
# decrypted = decrypt(encrypt, a, b)
# print('розшифровано:', decrypted)
