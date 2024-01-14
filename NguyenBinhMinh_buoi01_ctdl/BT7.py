def sum_of_digits(n):
# Trước tiên, kiểm tra nếu n nhỏ hơn 10. Nếu điều kiện này đúng, tức là n chỉ có một chữ số, hàm trả về giá trị n đó. Điều này là do tổng các chữ số của một số có một chữ số bằng chính nó.
    if n < 10:
        return n
# Trong trường hợp điều kiện ở bước 1 không đúng, hàm tính tổng của chữ số cuối cùng (n % 10) và gọi lại chính nó với tham số n // 10. Điều này tạo ra một lời gọi đệ quy, tính tổng các chữ số của phần còn lại của n sau khi loại bỏ chữ số cuối cùng.
    else:        
        return n % 10 + sum_of_digits(n // 10)
# Dòng tiếp theo của mã yêu cầu người dùng nhập một số nguyên dương (num). Nếu num nhỏ hơn hoặc bằng 0, hiển thị thông báo "Vui lòng nhập một số nguyên dương."
num = int(input("Nhập một số nguyên dương: "))
if num <= 0:
    print("Vui lòng nhập một số nguyên dương.")
#  Ngược lại, hàm sum_of_digits được gọi với giá trị num là tham số để tính toán tổng các chữ số. Kết quả được gán vào biến result.
else:
    result = sum_of_digits(num)
# Cuối cùng, giá trị của biến result được in ra bằng lệnh print, hiển thị tổng các chữ số của số nguyên dương đã nhập vào.
    print(result)