import re
i = input('Enter paragraph: ')
result1 = re.findall(r'\s(0+\d{9})', i)
result2 = re.findall(r'\S84+\d{9}', i)
print(result1, result2)
