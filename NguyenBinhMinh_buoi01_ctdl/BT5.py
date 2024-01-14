def factorial(n):
# Dòng đầu tiên sử dụng một câu lệnh assert để kiểm tra xem giá trị n có lớn hơn hoặc bằng 0 và có phải là số nguyên không. Nếu điều kiện này không đúng, một lỗi sẽ được phát sinh với thông điệp "The number must be positive integer only!". Trong trường hợp này, điều kiện đúng là n là số nguyên dương.
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
# Tiếp theo, kiểm tra nếu n có giá trị là 0 hoặc 1. Nếu điều kiện này đúng, tức là n bằng 0 hoặc 1, hàm sẽ trả về 1. Điều này đặc biệt vì giai thừa của 0 và 1 đều bằng 1.
    if n in [0,1]:
        return 1
# Trong trường hợp điều kiện ở bước 2 không đúng, hàm sẽ gọi lại chính nó với tham số n-1. Điều này tạo ra một lời gọi đệ quy, giảm giá trị n đi 1 và tính giai thừa của số n-1.
    else:
        return n * factorial(n-1)
# Dòng tiếp theo của mã yêu cầu người dùng nhập một số nguyên dương (num). Giá trị của num được truyền vào hàm factorial để tính toán giai thừa. Kết quả của hàm được gán vào biến result.
num = int(input("Nhập một số nguyên dương: "))
result = factorial(num)
# Cuối cùng, giá trị của biến result được in ra bằng lệnh print, hiển thị kết quả tính toán giai thừa của số nguyên dương đã nhập vào.
print(result)