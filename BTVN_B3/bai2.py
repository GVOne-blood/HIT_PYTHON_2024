# Bài 2:
# Cho một list a gồm k phần tử(a và k nhập từ bàn phím). Nhập vào hai số nguyên n, m là số dòng và số cột của một ma trận.
# Hãy xây dựng ma trận X(n × m) với các phần tử lần lượt lấy ra từ list ở trên (nếu có
# thể).
# Ví dụ: a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6], k = 18. Giả sử n = 3 và m =
# 4, ma trận x(3 × 4) thu được có dạng [[1, 2, 4, 3], [5, 4, 3, 6], [1, 4, 2, 7]]. Nhưng với
# n = 3, m = 7 ta không thể xây dựng được ma trận. In ra kết quả nếu có thể, không thì in ra “NO”
# #


a = list(map(int, input("Nhập các phần tử của list a, cách nhau bởi dấu cách: ").split()))
k = len(a)
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))


if len(a) < n * m:
         "NO"
    
result = []
for i in range(n):
        row = a[i * m:(i + 1) * m]
        result.append(row)
    

if result == "NO":
    print("NO")
else:
    for row in result:
        print(row)

