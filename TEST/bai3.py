n = 5
d = {
    'Khanh' : 73,
    'Hoang' : 51, 
    'Phuong' : 58,
    'Duy' : 93,
    'Hoa' : 81,
}
MIN = d.get('Khanh')
for key, value in d.items():
    if (value < MIN) : 
        MIN = value
        result = key
print(result)
