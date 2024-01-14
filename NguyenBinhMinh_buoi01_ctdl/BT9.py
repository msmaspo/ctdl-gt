def gcd(a, b):
# Trước tiên, kiểm tra nếu b bằng 0. Nếu điều kiện này đúng, tức là b là 0, hàm trả về giá trị của a. Điều này là do ước số chung lớn nhất giữa một số và 0 là chính nó.    
    if b == 0:
        return a
# Trong trường hợp điều kiện ở bước 1 không đúng, hàm tính ước số chung lớn nhất bằng cách gọi lại chính nó với tham số b và a % b. Điều này tạo ra một lời gọi đệ quy, trong đó a được thay thế bằng b và b được thay thế bằng phần dư của a chia b.
    else:       
        return gcd(b, a % b)
# Dòng tiếp theo của mã yêu cầu người dùng nhập hai số nguyên dương (num1 và num2).
num1 = int(input("Nhập số nguyên dương thứ nhất: "))
num2 = int(input("Nhập số nguyên dương thứ hai: "))
# Nếu num1 hoặc num2 nhỏ hơn hoặc bằng 0, hiển thị thông báo "Nhập hai số nguyên dương."
if num1 <= 0 or num2 <= 0:
    print("Nhập hai số nguyên dương.")
# Tính GCD sử dụng hàm đệ quy
else:
    result = gcd(num1, num2)
# In kết quả ra màn hình
    print(f"GCD của {num1} và {num2} là {result}")