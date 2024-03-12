class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy_head = ListNode()
    current = dummy_head

    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy_head.next

def display_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example Usage:
# Creating two sorted linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print("List 1:")
display_linked_list(list1)

print("List 2:")
display_linked_list(list2)

merged_list = merge_sorted_lists(list1, list2)

print("Merged Sorted List:")
display_linked_list(merged_list)
