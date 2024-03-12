class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def partition_linked_list(head, x):
    if not head:
        return None

    less_than_x = ListNode()  # Head of the list containing nodes less than x
    greater_than_x = ListNode()  # Head of the list containing nodes greater than or equal to x

    less_current = less_than_x
    greater_current = greater_than_x

    current = head

    while current:
        if current.value < x:
            less_current.next = current
            less_current = less_current.next
        else:
            greater_current.next = current
            greater_current = greater_current.next

        current = current.next

    # Combine the two partitions
    less_current.next = greater_than_x.next
    greater_current.next = None  # Set the end of the list for the greater partition

    return less_than_x.next  # Head of the combined list

# Helper function to display linked list
def display_linked_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example Usage:
# Creating a sample linked list
head = ListNode(11, ListNode(111, ListNode(222, ListNode(9, ListNode(333, ListNode(10, ListNode(444)))))))

# Partitioning the linked list around x = 10
x = 10
result_head = partition_linked_list(head, x)

# Displaying the result
display_linked_list(result_head)
