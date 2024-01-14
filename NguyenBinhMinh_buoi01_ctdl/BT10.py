def decimal_to_binary(n):
# Trước tiên, kiểm tra nếu n bằng 0. Nếu điều kiện này đúng, tức là n là 0, hàm trả về một chuỗi rỗng. Điều này là do khi n là 0, không có chữ số nào trong hệ nhị phân.  
    if n == 0:
        return ""
# Trong trường hợp điều kiện ở bước 1 không đúng, hàm chuyển đổi n sang hệ nhị phân bằng cách gọi lại chính nó với tham số n // 2 và nối kết quả với chuỗi biểu diễn của phần dư n % 2.
    else:       
        return decimal_to_binary(n // 2) + str(n % 2)
# Dòng tiếp theo của mã yêu cầu người dùng nhập một số nguyên dương (decimal_number) trong hệ thập phân.
decimal_number = int(input("Nhập một số nguyên hệ thập phân: "))
# Kiểm tra xem số nhập vào có là số nguyên không âm không
if decimal_number < 0:
    print("Nhập một số nguyên không âm.")
else:
# Gọi hàm để chuyển đổi số sang hệ nhị phân
    binary_result = decimal_to_binary(decimal_number)
# Cuối cùng, giá trị của biến binary_result được in ra bằng lệnh print, hiển thị số decimal_number ở dạng hệ nhị phân.  
    print(f"{decimal_number} ở hệ nhị phân là: {binary_result}")