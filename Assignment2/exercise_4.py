def leap():
    year = int(input('Enter year: '))
    if year % 4 == 0 and year % 100 or year % 400 == 0:
        print('THis is a leap year')
    else:
        print('This is not a leap year')
leap()