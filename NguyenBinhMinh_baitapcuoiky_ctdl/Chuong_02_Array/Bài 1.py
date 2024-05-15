def DoiXung(mang):
    # Kiểm tra số hàng và số cột của ma trận
    n = len(mang)
    m = len(mang[0])
    
    # Kiểm tra ma trận có phải là ma trận vuông hay không
    if n != m:
        return False
    
    # Kiểm tra tính đối xứng của ma trận
    for i in range(n):
        for j in range(m):
            if mang[i][j] != mang[j][i]:
                return False
    
    return True