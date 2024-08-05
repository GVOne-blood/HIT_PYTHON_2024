n = 5
a = [1, 2, 3, 4, 5]
b = a.copy()  
l = len(a)
m = max(a)
for i in range(1, m + 1):
    a.append(i)
a.sort()
b.sort()
re = set(a)
result = list(re)
print(result)
z = len(b)
for i in range(z, m, 1):
    b.append(0)
dem = 0
print(b)
for i in range(1, m):
    if result[i] in result and result[i] not in b:
            dem += 1
            #print(result[i])
    if dem == l :
        print(result[i])
        break

if dem < l:
    print(m + (l - dem))
