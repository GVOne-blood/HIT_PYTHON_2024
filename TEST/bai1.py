t = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4)
dem = {}
for i in range(len(t)):
    if t[i] not in dem:
        dem[t[i]] = 0
    dem[t[i]] += 1

for i in dem:
    if dem[i] % 5 == 0 and dem[i] % 10 != 0:
        print(i)
##