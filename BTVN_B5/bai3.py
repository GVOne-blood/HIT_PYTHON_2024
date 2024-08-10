import random as rd

while True:
    n = int(input('nhap n : '))
    if 10 <= n <= 100000:
        break

dict = {}
major = ['CNTT', 'KHMT', 'KTPM', 'HTTT']

for i in range(n):
    dict['Account{}'.format(i + 1)] = {
        'Username': 2023600000 + i + 1,
        'Password': rd.choice(major) + str(2023600000 + i + 1),
    }

print(dict)
