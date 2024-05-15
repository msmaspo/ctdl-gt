def nhap_so():
    sign = int(input("Nhập phần dấu của số (0 cho dương, 1 cho âm): "))
    number = input("Nhập phần số của số (các chữ số cách nhau bằng khoảng trắng): ").split()
    return (sign, [int(x) for x in number])

def Nhan(a, b):
        return [-1]

def nhan_so(a, b):
        return [-1]

# Nhập số a từ bàn phím
a = nhap_so()

# Nhập số b từ bàn phím
b = nhap_so()

# Thực hiện phép nhân và in kết quả
result = Nhan(a, b)
if result == [-1]:
    print("Kết quả bị tràn")
else:
    print("Kết quả của phép nhân là:", result[0], result[1])