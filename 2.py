from math import *


def CalculateSquareRoot(Number):
    return sqrt(Number)


def append_item(item, l=[]):
    l.append(item)
    return l


while True:
    try:
        your_number = float(input("Enter your number: "))
        print("Square root is:", CalculateSquareRoot(your_number))
        break
    except:
        pass

massiv = [1, 2, 3]

slovar = {key1: 1, key2: 2, key3: 3, key4: 4, key5: 5}

slovar2 = {
    key1: 1,
    key2: 2,
    key3: 3,
    key4: 4,
    key5: 5,
}

