from array import *

def Nhan(a, b):

    len_a = len(a)
    len_b = len(b)
    result_length = len_a + len_b
    result = array('i', [0] * result_length)

    if result_length > 10:
        return array('i', [-1] * 10)

    for i in range(len_a - 1, -1, -1):
        carry = 0  
        for j in range(len_b - 1, -1, -1):
    
            product = a[i] * b[j] + result[i + j + 1] + carry
            result[i + j + 1] = product % 10 
            carry = product // 10  
        result[i] += carry  

   
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result

a = array('i', [1, 2, 3])
b = array('i', [4, 5, 6])
print(Nhan(a, b))  

