class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_intersection_node(head1, head2):
    
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    length1 = get_length(head1)
    length2 = get_length(head2)

    while length1 > length2:
        head1 = head1.next
        length1 -= 1

    while length2 > length1:
        head2 = head2.next
        length2 -= 1

    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next

    return None 

# Example Usage:
list1 = ListNode(3, ListNode(1, ListNode(5, ListNode(9))))
list2 = ListNode(2, ListNode(4, ListNode(6)))
intersection = ListNode(7, ListNode(2, ListNode(1)))

list1.next.next.next.next = intersection
list2.next.next.next = intersection

result = get_intersection_node(list1, list2)

if result:
    print("Intersecting Node Value:", result.value)
else:
    print("No intersection")
