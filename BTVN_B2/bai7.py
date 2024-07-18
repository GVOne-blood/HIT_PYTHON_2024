# Bài 7: Viết một chương trình nhận vào một số N từ người dùng và in ra tất cả các cặp số Amicable từ 1 đến N.
# Cặp số Amicable là cặp số mà tổng các ước số của số thứ nhất bằng số thứ hai và ngược lại.
def sumOfUoc(n) :
    sum = 0
    for i in range(1, n) :
        if n % i == 0 :
            sum += i
    return sum
n = int(input('nhap n : '))
for i in range(1, (n + 1)) :
    sum = sumOfUoc(i)
    if sumOfUoc(sum) == i and sum < i :
        print(i, ' ', sum)  