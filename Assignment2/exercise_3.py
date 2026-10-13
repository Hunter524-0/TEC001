def hemoglobin():
    gender = input('Male or Female: ')
    hemoglobin = float(input('Enter your hemoglobin: '))
    if gender == 'Male':
        if hemoglobin < 134:
            print('Low')
        elif hemoglobin >= 134 and hemoglobin <= 167:
            print('Normal')
        else:
            print('High')
    elif gender == 'Female':
        if hemoglobin < 117:
            print('Low')
        elif hemoglobin >= 117 and hemoglobin <= 155:
            print('Normal')
        else:
            print('High')
    else:
        print('Invalid gender')
hemoglobin()