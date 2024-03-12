class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_lists(list1, list2):
    dummy_head = ListNode() 
    current = dummy_head
    carry = 0

    while list1 or list2 or carry:
    
        value1 = list1.value if list1 else 0
        value2 = list2.value if list2 else 0

        total_sum = value1 + value2 + carry

        carry = total_sum // 10

        current.next = ListNode(total_sum % 10)
        current = current.next

        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next

    return dummy_head.next

def display_linked_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example Usage:
list1 = ListNode(7, ListNode(1, ListNode(6)))
list2 = ListNode(5, ListNode(9, ListNode(2)))

result = add_lists(list1, list2)

display_linked_list(result)
