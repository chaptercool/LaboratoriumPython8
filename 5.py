def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if a == 0 or b == 0:
        None
    else:
        return a / b

dict_calc = {'+': dodawanie, '-': odejmowanie, '*': mnozenie, '/': dzielenie}

x = input(("Podaj typ operacji: "))
a = int(input("Proszę o podaniu pierwszej liczby: "))
b = int(input("Proszę o podaniu drugiej liczby: "))

print(dict_calc[x](a, b))