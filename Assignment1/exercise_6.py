talent = int(input('Talent: '))
pound = int(input('Pound: '))
lot = int(input('Lot: '))
talent_to_gram = talent * 20 * 32 * 13.3
pound_to_gram = pound * 32 * 13.3
lot_to_gram = lot * 13.3
total_gram = talent_to_gram + pound_to_gram + lot_to_gram
kilogram = (total_gram / 1000)
gram= total_gram - kilogram * 1000
print(f'Kilogram: {kilogram} and gram: {gram}')
