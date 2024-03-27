def TrungHang(mang):
    # Kiểm tra số hàng và số cột của ma trận
    n = len(mang)
    m = len(mang[0])
    
    # Kiểm tra tính trùng hàng của ma trận
    for i in range(n):
        for j in range(i + 1, n):
            if mang[i] == mang[j]:
                return True
    
    return False