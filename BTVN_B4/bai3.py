happy = 0
n, m = map(int, input('nhap n va m  : ').split())
S = set(map(int, input('nhap S : ').split()[:n]))
A = set(map(int, input('nhap A : ').split()[:m]))
B = set(map(int, input('nhap B : ').split()[:m]))
if (S & A) :
    happy += len(S & A)
if (S & B) :
    happy -= len(S & B)
print('muc do happy : ', happy)
