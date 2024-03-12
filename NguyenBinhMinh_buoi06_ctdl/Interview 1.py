class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head or not head.next:
        return head

    seen_values = {head.value}
    current_node = head

    while current_node.next:
        if current_node.next.value in seen_values:
            current_node.next = current_node.next.next
        else:
            seen_values.add(current_node.next.value)
            current_node = current_node.next

    return head

def display_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.value, end=" -> ")
        current_node = current_node.next
    print("None")

# Example Usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, ListNode(4))))))

print("Original Linked List:")
display_linked_list(head)

remove_duplicates(head)

print("\nLinked List after Removing Duplicates:")
display_linked_list(head)
