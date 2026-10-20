i = 0
while i < 5:
    names = input('Username: ')
    passes = input('Password: ')
    if names == 'python' and passes == 'rules':
        print('Welcome')
        break
    elif i == 5:
        break
    else:
        print('Wrong')
        i = i + 1