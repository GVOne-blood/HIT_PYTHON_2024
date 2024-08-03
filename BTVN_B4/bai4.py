n = int(input('nhap n : '))
a = set(map(int, input('nhap a : ').split()[:n]))
k = int(input('nhap k : '))
b = set()
sum = 0
for i in a : 
    sum += i
    b.add(i)
    if sum > k :
        sum -= b.pop()
    if sum == k :
        break
print(b)

        
