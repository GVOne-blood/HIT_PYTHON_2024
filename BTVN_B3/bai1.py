# Bài 1:
# Nhập vào một list có N phần tử là số nguyên.(N nhập từ bàn phím):
# Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
# Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3].
# Sử dụng list sau khi thay thế để giải quyết các bài toán tiếp theo.
# Tìm số lớn nhất, và nhỏ nhất trong list.
# Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
# Sau khi chèn số Y, kiểm tra các số trong list có sắp xếp theo thứ tự tăng dần hay giảm dần không.
# Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIÁM”,
# nếu không tăng không giảm thì in “NO”.
# Tạo một list mới có N phần tử. Các phần tử sẽ có vị trí từ 1 -> N. Với mỗi phần tử ở vị trí i (1 <= i <= N) 
# giá trị của nó là tổng i phần tử đầu tiên của list cũ.
# Tạo một list mới [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000] và sắp xếp nó theo thứ tự tăng dần của giá trị, 
# và sắp xếp nó theo sự tăng dần của giá trị tuyệt đối.
n = int(input('nhap n : '))
#l = [int(input()) for _ in range(n)]
l = [x for x in range(0, n+1)]
print(l)
x = int(input('nhap x : '))
print('xuat hien {} lan trong list'.format(l.count(x)))
l[2:7] = [8, 5, 4, 0, 1, 3]
print('list sau khi thay doi : ', l)
a = l;
a.sort()
print('min element : ', a[0])
print('max element : ', a[-1])
del a
y = int(input('nhap y : '))
l.insert(y, 0)
print('list sau khi chen : ', l)
if sorted(l) == l:
    print('TANG')
elif sorted(l, reverse=True) == l:
    print('GIAM')
else :
    print('NO')
new_l = []
for i in range(1, len(l), 1):
    new_l.append(sum(l[:i - 1]))
print(new_l)
new_l2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
new_l2.sort()
print('list sau khi sap xep : ', new_l2)
new_l2 = sorted(new_l2, key=abs)
print('list sau khi sap xep theo gia tri tuyet doi : ', new_l2)

  



