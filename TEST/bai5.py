n = 5
a = [1, 3, 2, 6, 10]
b = a.copy()  
l = len(a)
m = max(a)
for i in range(1, m):
    a.append(i)
a.sort()
b.sort()
re = set(a)
result = list(re)
for i in range(len(a), m):
    b.append(0)
dem = 0
for i in range(1, m):
    if result[i] in result and result[i] not in b:
        if dem == l - 1:
            print(result[i])
        else:
            dem += 1


if dem > l:
    print(m + 1)
