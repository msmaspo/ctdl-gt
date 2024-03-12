class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def nth_to_last(head, n):
    if not head or n < 1:
        return None

    pointer1 = pointer2 = head

    for _ in range(n):
        if not pointer2:
            return None 
        pointer2 = pointer2.next

    while pointer2.next:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1.value

# Example Usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

n = 2
result = nth_to_last(head, n)

if result is not None:
    print(f"The {n}th to last element is: {result}")
else:
    print(f"There is no {n}th to last element.")
