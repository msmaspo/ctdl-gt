def power(base, exponent):
# Trước tiên, kiểm tra nếu exponent bằng 0. Nếu điều kiện này đúng, tức là số mũ là 0, hàm trả về 1. Điều này là do bất kỳ số nào mũ 0 đều bằng 1.
    if exponent == 0:
        return 1
# Trong trường hợp điều kiện ở bước 1 không đúng, hàm tính lũy thừa bằng cách nhân base với giá trị trả về của lời gọi đệ quy power(base, exponent - 1). Điều này tạo ra một lời gọi đệ quy, giảm giá trị của exponent đi 1 và tính lũy thừa của base với số mũ exponent - 1.
    else:       
        return base * power(base, exponent - 1)
# Dòng tiếp theo của mã yêu cầu người dùng nhập giá trị cơ sở (base) dưới dạng số thực và số mũ (exponent) dưới dạng số nguyên. Giá trị của base và exponent được truyền vào hàm power để tính giá trị lũy thừa. Kết quả được gán vào biến result.
base = float(input("Nhập giá trị cơ sở (base): "))
exponent = int(input("Nhập số mũ (exponent): "))
# Tính lũy thừa sử dụng hàm đệ quy
result = power(base, exponent)
# Cuối cùng, giá trị của biến result được in ra bằng lệnh print, hiển thị giá trị lũy thừa của base với số mũ exponent.
print(f"{base}^{exponent} = {result}")