def zan_len():
    zander = float(input('Enter zander length: '))
    if zander < 42:
        print(f'Fish got released and your zander need to be {42 - zander}')
    else:
        print('Fish caught')
zan_len()