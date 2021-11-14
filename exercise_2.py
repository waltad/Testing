"""Zadanie 2
Masz kod:
def odd_indexes(string):
    return string[1::2]
który dla zadanego stringa zwraca litery z nieparzystych indeksów, np:
teleturniej -> eeune komputer -> optr
Przetestuj tę funkcję dla argumentu, który będzie stringiem.
Uruchom funkcję przekazując int. Zaobserwuj, co się stało. Napisz testy dla argumentów, które są intem. Popraw funkcję
 by działała poprawnie, sprawiając by testy przeszły.
Podpowiedź
Funkcja str() pozwala zamienić element przekazany do niej na string."""


def odd_indexes(string):
    string = str(string)
    return string[1::2]


if __name__ == '__main__':
    string1 = 'teleturniej'
    string2 = 'komputer'
    print(odd_indexes(string1))
    print(odd_indexes(string2))
