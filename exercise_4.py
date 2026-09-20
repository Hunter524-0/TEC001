length = int(input('Enter length: '))
width = int(input('Enter width: '))
def rect(length):
    perimeter = (length + width) * 2
    area = length * width
    print(f'Perimeter: {perimeter}, Area: {area}')
rect(length)