config = {
    'n': 1500,
    'm': 2,
    'CLUSTERS': 3,
    'ITER': 10000,
    'METHOD': 'FCM',
    'MEASURE': 'EUCLIDEAN',
    'YEARS': 51
}

print('noi dung file config:', config)
config['MEASURE'] = 'MANHHATAN'
print('noi dung file config:', config)
config.get('LOSS FUNCTION', 'NORM_2')
print('noi dung file config:', config)
del config['YEARS']
print('noi dung file config:', config)
s = input('nhap s : ')
for key, value in config.items():
    if s == key :
        print('trung key {} '.format(key))

a = list(config.values())
print('Values -> list:', a)
a = set(config.values())
print('Values -> set:', a)