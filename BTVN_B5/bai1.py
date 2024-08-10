d = {
    '2022603565' : 3.05,
    '2022605709' : 3.67,
    '2022603566' : 3.45,
    '2022603567' : 3.25,
}
cnt = 0
for key in d.keys():
    if d[key] <= 3.5 and d[key] >= 3.0:
        cnt += 1
print('so sv co diem trong doan [3.0, 3.5] la', cnt)
key = input('nhap ma sv can them: ')
value = float(input('nhap diem can them: '))
d[key] = value
print('danh sach sau khi them:', d)
items = [key for key, value in d.items() if value < 2.0]
for key in items:
    del d[key]
print('danh sach sau khi xoa:', d)
