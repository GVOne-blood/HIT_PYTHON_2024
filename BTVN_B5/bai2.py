string = input('nhap chuoi :')
dict = {}

for i in string:
    dict[i] = dict.get(i, string.count(i))
print(dict)