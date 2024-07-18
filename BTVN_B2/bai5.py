# Bài 5: Nhập vào 1 số n. Viết chương trình in ra tất cả các số Armstrong bậc 3 từ 1 đến n. 
# (Số Armstrong bậc 3 là số mà tổng lập phương của các chữ số của nó bằng chính nó)
def check(n):
    a = 0
    m = n
    while n > 0:
        a += (n % 10) ** 3
        n //= 10
    return a == m
n = int(input('nhap n : '))
for i in range(1, n + 1) :
    if check(i) :
        print(i)
     

