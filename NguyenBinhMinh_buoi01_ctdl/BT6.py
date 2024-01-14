def fibonacci(n):
# Dòng đầu tiên sử dụng một câu lệnh assert để kiểm tra xem giá trị n có lớn hơn hoặc bằng 0 và có phải là số nguyên không. Nếu điều kiện này không đúng, một lỗi sẽ được phát sinh với thông điệp "Fibonacci number cannot be negative number or non integer."
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
# Tiếp theo, kiểm tra nếu n có giá trị là 0 hoặc 1. Nếu điều kiện này đúng, tức là n bằng 0 hoặc 1, hàm sẽ trả về n. Điều này là do số Fibonacci thứ 0 và thứ 1 đều bằng chính nó.
    if n in [0,1]:
        return n
# Trong trường hợp điều kiện ở bước 2 không đúng, hàm sẽ gọi lại chính nó hai lần với các tham số n-1 và n-2. Điều này tạo ra một lời gọi đệ quy, tính giá trị của số Fibonacci thứ n-1 và n-2.
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Dòng tiếp theo của mã yêu cầu người dùng nhập một số nguyên dương (num). Giá trị của num được truyền vào hàm fibonacci để tính toán giá trị của số Fibonacci thứ num. Kết quả của hàm được gán vào biến result.
num = int(input("Nhập một số nguyên dương: "))
result = fibonacci(num)
# Cuối cùng, giá trị của biến result được in ra bằng lệnh print, hiển thị giá trị của số Fibonacci tương ứng với số nguyên dương đã nhập vào.
print(result)
