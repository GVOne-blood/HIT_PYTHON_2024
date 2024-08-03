a = ('12342342', '2009453408','000423403')
b=list(a)
avg = 0
for i in range(len(b)):
    b[i]=int(b[i])
    avg += b[i]
b=tuple(b)
print('chuoi sau khi convert : ' , b)
print('trung binh cua chuoi : ', avg)
    
