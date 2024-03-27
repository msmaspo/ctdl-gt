
import numpy as np

def NhomHang(mang):
    n = len(mang)

    hang_list = [tuple(row) for row in mang]
    
    nhom_hang = {}
    
    for i, hang in enumerate(hang_list):
        if hang not in nhom_hang:
            nhom_hang[hang] = [i]
        else:
            nhom_hang[hang].append(i)
   
    for nhom, chi_muc in nhom_hang.items():
        print(f"Nhóm hàng giống nhau {nhom}: Chỉ mục hàng {chi_muc}")

mang = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
NhomHang(mang)
