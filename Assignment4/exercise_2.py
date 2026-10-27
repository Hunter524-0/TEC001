import re
while True:
    i = input('Enter hex color: ')
    if re.findall(r'^#[a-zA-Z0-9]{6}$', i):
        print('True')
    else:
        print('False')