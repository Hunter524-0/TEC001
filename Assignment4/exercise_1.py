import re
while True:
    i = input('Enter course: ')
    if re.findall(r'^[A-Z]{3}\d{3}$', i):
        print('True')
    else:
        print('False')