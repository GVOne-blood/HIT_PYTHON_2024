n = int(input('nhap n : '))
a = [(input()) for _ in range(n)]
b = tuple(a)
print(b)
c = [str(x) for x in range (0, 10)]
z = 0
cnt = 0
for i in b : 
    for j in i :
        if j in c :
            z += 1
    if z == len(i) :
        cnt += 1
    z = 0
print(cnt)
