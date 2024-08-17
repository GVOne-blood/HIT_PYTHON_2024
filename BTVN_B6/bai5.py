phone_number = input("Nhập số điện thoại: ")
numbers = ['0', '1', '2', '3', '4', '5' ,'6' ,'7' ,'8' ,'9']
l = []
for i in range(len(phone_number)):
    if phone_number[i] in numbers:
      l.append(phone_number[i])
if len(l) != 10 or l[0] != "0":
    print('Invalid phone number')
else :
    print('Phone number is : ',''.join(map(str, l)))
