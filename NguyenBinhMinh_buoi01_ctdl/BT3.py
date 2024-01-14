# Kiểm tra điều kiện n < 1. Nếu điều kiện này đúng, tức là n nhỏ hơn 1, hàm sẽ in ra thông báo "n is less than 1".
def recursiveMethod(n):
# Kiểm tra điều kiện n < 1. Nếu điều kiện này đúng, tức là n nhỏ hơn 1, hàm sẽ in ra thông báo "n is less than 1".
    if n<1:
        print("n is less than 1")
# Trong trường hợp điều kiện n < 1 không đúng, hàm sẽ gọi lại chính nó với tham số n-1. Điều này tạo ra một lời gọi đệ quy, giảm giá trị n đi 1 và tiếp tục thực hiện hàm recursiveMethod trên n-1.    
    else:
        recursiveMethod(n-1)
# Sau khi quay lại từ lời gọi đệ quy, hàm in ra giá trị hiện tại của n.        
        print(n)
# Dòng cuối cùng của mã yêu cầu người dùng nhập một số (num), sau đó gọi hàm recursiveMethod với giá trị num như là tham số.
num = int(input())
# Khi hàm recursiveMethod được gọi, nó sẽ thực hiện đệ quy, giảm giá trị n đi 1 cho đến khi n nhỏ hơn 1. Khi đó, các lời gọi đệ quy sẽ kết thúc và giá trị n sẽ được in ra từ giá trị nhỏ nhất đến giá trị lớn nhất.
recursiveMethod(num)