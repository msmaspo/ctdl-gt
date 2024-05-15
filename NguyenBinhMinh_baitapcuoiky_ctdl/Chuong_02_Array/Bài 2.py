def TamGiacTren(mang):
    # Kiểm tra số hàng và số cột của ma trận
    n = len(mang)
    m = len(mang[0])
    
    # Kiểm tra ma trận có phải là ma trận vuông hay không
    if n != m:
        return False
    
    # Kiểm tra tính tam giác trên của ma trận
    for i in range(n):
        for j in range(i+1, m):
            if mang[i][j] != 0:
                return False
    
    return True