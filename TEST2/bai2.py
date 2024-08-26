def num(n):
    a = 0
    sum = 0
    re = n
    while n > 0:
        a = n%10
        sum += a
        n //= 10
    if sum == 10: 
        return re
    else:
        return 0
k = int(input('nhap so hoan hao nho thu k :  '))
n = 10**k
dem = 0
result = 0
for i in range(10, n, 9):
    if (num(i) == i):
        dem += 1
    if dem == k:
        result = num(i)
        break 
print(result)
           
    