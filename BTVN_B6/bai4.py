dem = 1  # Khai báo biến 'dem' là biến toàn cục

def SSoN(n: int) -> int:
    tong = 0
    
    def SoN(n: int) -> list:
        if n < 0:
            return 0
        elif n < 10:
            return n
        else:
            return SoN(n // 10) + (n % 10)
    if n < 10 : 
        return 1, n
    else :
        tong = SoN(n)
        global dem 
        dem += 1
        while (tong >= 10): 
            dem += 1
            tong = SoN(tong)
    
    return dem, tong

n = int(input("Nhập số nguyên dương n = "))
result = SSoN(n)
print(result)
