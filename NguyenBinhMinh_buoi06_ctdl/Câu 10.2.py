class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.value == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next

def display_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = None

print("Original Linked List:")
display_linked_list(head)

val_to_remove = 1
head = remove_elements(head, val_to_remove)

print(f"Linked List After Removing Elements with Value {val_to_remove}:")
display_linked_list(head)
