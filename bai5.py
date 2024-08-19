phone_number = input("Nhập số điện thoại: ")
numbers = ['0', '1', '2', '3', '4', '5' ,'6' ,'7' ,'8' ,'9']
def format_phone_number(phone_number):
    l = []
    for i in range(len(phone_number)):
        if phone_number[i] in numbers:
            l.append(phone_number[i])
    if len(l) != 10 or l[0] != "0":
        return 'Invalid phone number'
    else :
        return ''.join(map(str, l))
#
print(format_phone_number(phone_number))

