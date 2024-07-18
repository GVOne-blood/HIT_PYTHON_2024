# Bài 9: Cho một số a bất kỳ
# a. Trả về số lượng các bits cần thiết để biểu diễn số a ở dạng nhị phân, 
# không bao gồm phần dấu và các số 0 ở đầu.
# b. Với biến x = “awesome”, sử dụng 3 cách print để cùng đưa ra màn hình “Python is awesome”
# c. Viết chương trình kiểm tra version của python hiện tại

# a)
a = int(input('nhap a : '))
dem = 0
while a != 0 : 
    a //= 2
    dem += 1
print (dem)
# b)
x = 'awesome'
print ('Python is', x)
print ('Python is {}'.format(x))
print(f'Python is {x}')
# c)
import sys
print (sys.version)