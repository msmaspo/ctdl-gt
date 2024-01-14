# Hàm nhận một tham số doll, đại diện cho số lượng búp bê Nga cần mở.
def openRussianDoll(doll):
# Nếu doll bằng 1, nghĩa là chỉ còn một chiếc búp bê Nga cuối cùng, thì sẽ in ra thông báo "All dolls are opened" (Tất cả các búp bê đã được mở).
    if doll == 1:
        print("All dolls are opened")
# Trong trường hợp doll không bằng 1, tức là còn nhiều hơn một chiếc búp bê Nga, hàm sẽ gọi lại chính nó với tham số doll-1, để mở búp bê nhỏ hơn trong tập hợp.
    else:
        openRussianDoll(doll-1)
        print("All doll are closed")
# Nhập dữ liệu từ người dùng với hàm input.
doll = int(input())
openRussianDoll(doll)