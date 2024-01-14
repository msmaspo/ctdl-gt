def powerOfTwo(n):
# Kiểm tra điều kiện n == 0. Nếu điều kiện này đúng, tức là n bằng 0, hàm sẽ trả về giá trị 1. Điều này đặc biệt vì 2 mũ 0 luôn bằng 1.
    if n == 0:
        return 1
# Trong trường hợp điều kiện n == 0 không đúng, hàm sẽ gọi lại chính nó với tham số n-1. Điều này tạo ra một lời gọi đệ quy, giảm giá trị n đi 1 và tính toán lũy thừa của 2 với số mũ n-1.
    else:
        power = powerOfTwo(n-1)
# Sau khi quay lại từ lời gọi đệ quy, hàm nhân giá trị trả về của lời gọi đệ quy (power) với 2 và trả về kết quả.
        return power * 2
# Dòng tiếp theo của mã yêu cầu người dùng nhập một số (num), sau đó gọi hàm powerOfTwo với giá trị num như là tham số. Kết quả trả về của hàm được gán vào biến a.
num =int(input())
a = powerOfTwo(num)
# Cuối cùng, giá trị của biến a được in ra bằng lệnh print, hiển thị kết quả lũy thừa của 2 với số mũ là giá trị nhập vào.
print(a)