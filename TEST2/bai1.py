n = input('Enter a string: ')
i = 0
j = 0
a = 0
total_sum = 0
check = True
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while i < len(n):
    if check and n[i] == '-':
        j += 1
        check = False
    while n[i] in num and j < len(n):
        j += 1
    if n[i] == '-':
        a = -int(n[i:j])
    else:
        a = int(n[i:j])
    total_sum += a
    i += 1

print('The sum is:', total_sum)
