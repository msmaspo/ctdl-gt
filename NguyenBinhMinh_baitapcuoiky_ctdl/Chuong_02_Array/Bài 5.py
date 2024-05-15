def Cong(a, b):

    len_a, len_b = len(a), len(b)
    
    max_len = max(len_a, len_b) + 1
    
    result = [0] * max_len
    carry = 0
   
    for i in range(max_len):
        
        val_a = a[i] if i < len_a else 0
        val_b = b[i] if i < len_b else 0
        
        temp_sum = val_a + val_b + carry
        result[i] = temp_sum % 10
        carry = temp_sum // 10
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

a = [1, 2, 3]  
b = [4, 5, 6]  
result = Cong(a, b)
print("Kết quả:", result)
