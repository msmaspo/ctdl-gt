
def Tru(a, b):
    len_a, len_b = len(a), len(b)
    
    max_len = max(len_a, len_b)
    result = [0] * max_len
    borrow = 0
    
    for i in range(max_len):
        val_a = a[i] if i < len_a else 0
        val_b = b[i] if i < len_b else 0

        temp_diff = val_a - val_b - borrow
        if temp_diff < 0:
            temp_diff += 10
            borrow = 1
        else:
            borrow = 0
        result[i] = temp_diff
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


a = [7, 8, 5, 2] 
b = [2, 6, 4, 3]        
result = Tru(a, b)
print("Kết quả:", result)
