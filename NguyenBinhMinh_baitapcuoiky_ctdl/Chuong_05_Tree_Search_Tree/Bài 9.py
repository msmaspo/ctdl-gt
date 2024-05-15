class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def CayCon(cay1, cay2):
    if not cay2:  # Nếu cây con là None, luôn là cây con của cây gốc
        return True
    if not cay1:  # Nếu cây gốc là None nhưng cây con không phải, không thể là cây con
        return False
    # Kiểm tra từng nút của cây gốc
    return (
        (cay1.info == cay2.info) and
        CayCon(cay1.left, cay2.left) and
        CayCon(cay1.right, cay2.right)
    )

# Ví dụ sử dụng
# Tạo cây 1
cay1 = Node(1)
cay1.left = Node(2)
cay1.right = Node(3)
cay1.left.left = Node(4)
cay1.left.right = Node(5)

# Tạo cây 2
cay2 = Node(2)
cay2.left = Node(4)
cay2.right = Node(5)

# Kiểm tra xem cây 2 có phải là cây con của cây 1 không
print(CayCon(cay1, cay2))  # Kết quả sẽ là True
