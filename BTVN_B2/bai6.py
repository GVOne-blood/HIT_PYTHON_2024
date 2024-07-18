# Bài 6: Nhập vào 1 số n. 
# In ra tất cả các số hoàn hảo từ 1 đến n. 
# ( Số hoàn hảo là số mà tổng các ước của nó (không tính chính nó) bằng chính nó ).
def findUoc(n) : 
    sum = 0
    for i in range(1, n // 2 + 1) :
        if (n % i == 0) : 
            sum += i
    return sum == n
n = int(input('nhap n : '))
if (n < 6) :
    print('khong co so hoan hao trong doan tu 1 - ', n)
for i in range(1, n + 1) :
    if findUoc(i) : 
        print(i, end=' ')