# Bài 1: Tính tổng các chữ số trong một số nguyên dương
# Viết một chương trình yêu cầu người dùng nhập một số nguyên dương. 
# Tính và in ra tổng các chữ số của số đó. Ví dụ: Đối với số 12345, 
# tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15.
# Tính tổng các ước số của một số nguyên dương:
# Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n. 
# Tính và in ra tổng của tất cả các ước số của n. Ước số của một số là các số mà chia hết cho số 
# đó mà không dư. Ví dụ: Ước số của 6 là 1, 2, 3, và 6.
# Kiểm tra tam giác:
# Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương.
#  Kiểm tra xem 3 số đó có tạo thành tam giác hay không? 
#  Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)
# a)
n = int(input('nhap n : '))
sum = 0
while n % 10 != 0:
    sum += n % 10
    n //= 10
print(sum)
# b)
n = int(input('nhap n : '))
sum = 0
for i in range(1, (int)(n / 2) + 1):
    if n % i == 0 :
     sum += i
     print(i, ' ', ' ')
print(sum)
# c)
print('nhap a, b, c : ')
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b :
    if a == b == c : 
        print('tam giac deu')
    elif a == b != c :
        print('tam giac can')
    elif a*a > b*b + c*c and b*b > a*a + c*c and c*c > a*a + b*b :
        print('tam giac tu')
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b :
        print('tam giac vuong')
    else :
        print('tam giac nhon')
else :
    print('khong the tao thanh tam giac')