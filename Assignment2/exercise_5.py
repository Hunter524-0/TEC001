import math
def value(diameter, price):
    area = math.pi * ((diameter / 2 / 100) ** 2)
    return price / area
def prof():
    d1 = float(input('Enter 1st pizza diameter: '))
    p1 = float(input('Enter price: '))
    d2 = float(input('Enter 2nd pizza diameter: '))
    p2 = float(input('Enter price: '))
    pizza1 = value(d1, p1)
    pizza2 = value(d2, p2)
    if pizza1 < pizza2:
        print('The 1st pizza provide better value')
    else:
        print('The 2nd pizza provide better value')
prof()