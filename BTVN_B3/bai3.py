# Nhập 2 chuỗi s1, s2 từ bàn phím:
# In ra đảo ngược của chuỗi s1
# Nhập vào 2 số nguyên a, b (1 <=a < b <= len(s2)). In ra chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b.
# In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn
# Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
# VD: s1 = “abc”, s2 = “123” -> s4 = “a1b2c3”
# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
# VD: s1 = “set”, s2 = “bit” -> “bet” và “sit”
import math
s1 = input('Nhập chuỗi s1: ')
s2 = input('Nhập chuỗi s2: ')

print('Chuỗi đảo ngược của', s1, ':', s1[::-1])

while True:
    a = int(input('Nhập số nguyên a: '))
    b = int(input('Nhập số nguyên b: '))
    if 1 <= a < b <= len(s2):
        break
    else:
        print('Vi phạm điều kiện nhập')

print('Chuỗi đảo ngược từ vị trí', a, 'đến', b, 'của', s2, ':')
print(s2[:a-1], s2[a-1:b-1:-1], s2[b:], sep='    ')
s3 = s1[::2]
print('chuoi sau khi xoa cac ky tu o vi tri chan ', s3)

for i in range(max(len(s1), len(s2)) - 1) : 
    s3 += s1[i] + s2[i];
print('chuoi sau khi tron', s3)
temp = s1[0]
s1 = s2[0] + s1[1::]
s2 = temp + s2[1::]

print('chuoi sau khi doi cho 2 ky tu dau tien : ', s1,'\n', s2)


