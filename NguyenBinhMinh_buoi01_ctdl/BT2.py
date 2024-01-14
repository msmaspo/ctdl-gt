# Hàm firstMethod được định nghĩa đầu tiên. Nó gọi hàm secondMethod bằng cách viết secondMethod(), sau đó in ra chuỗi "I am the first Method" bằng lệnh print.
def firstMethod():
    secondMethod()
    print("I am the first Method")
# Hàm secondMethod được định nghĩa tiếp theo. Nó gọi hàm thirdMethod bằng cách viết thirdMethod(), sau đó in ra chuỗi "I am the second Method".
def secondMethod():
    thirdMethod()
    print("I am the second Method")
# Hàm thirdMethod được định nghĩa tiếp theo. Nó gọi hàm fourthMethod bằng cách viết fourthMethod(), sau đó in ra chuỗi "I am the third Method".
def thirdMethod():
    fourthMethod()
    print("I am the third Method")
# Hàm fourthMethod được định nghĩa cuối cùng. Nó chỉ in ra chuỗi "I am the fourth Method".
def fourthMethod():
    print("I am the fourth Method")
# Cuối cùng, khi firstMethod được gọi, các hàm secondMethod, thirdMethod, và fourthMethod sẽ được gọi tuần tự theo thứ tự như đã định nghĩa.
firstMethod()