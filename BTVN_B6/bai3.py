import math
def caculate (operation : str, *args) -> float:
    if operation == 'add': 
        return sum(args)
    elif operation == 'multiply':    
        return math.prod(args)
    elif operation == 'max':
        return max(args)
    elif operation == 'min':
        return min(args)
    else :
        return 'Invalid operation'
print(caculate ('max', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    