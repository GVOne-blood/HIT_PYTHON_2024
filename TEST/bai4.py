# l = input().split(',')
# print(l)
# for i in l:
#     i = i.split()
# result = set(l)
# print(list(result))
l = input().split(',')
print(l)
for i in l:
    letter = set(i)
    for char in letter:
        print(char)
print()
