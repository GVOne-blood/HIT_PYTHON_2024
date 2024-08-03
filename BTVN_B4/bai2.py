A = {1, 2, 3, 4, 5, 6}
B = {10, 8, 6, 5, 7, 9}
print(A)
print(B)
if A & B : 
    print('co sv chung ')
else :
    print('khong co sv chung')
print('sv chung la : ', A&B)
print('sv o ban 1 ma kh o ban 2 la : ', (A - (A&B)))


