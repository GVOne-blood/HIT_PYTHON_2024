# Bài 4:  Dãy số Fibonacci
# Hãy viết chương trình tìm n số Fibonacci đầu tiên.
# Quy luật của dãy số Fibonacci: 
#     số tiếp theo bằng tổng của 2 số trước, 2 số đầu tiên của dãy số là 0, 1. 
#     Ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

n = int(input('nhap n > 0: '))
f0 = 0
f1 = 1
if n >= 2 :
    print (f0, f1, end=' ')
elif n == 1 : 
    print(f0) 

for i in range(n - 2) : 
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        print(f2, end=' ')