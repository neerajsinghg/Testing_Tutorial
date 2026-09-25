"""
Interview Question: How do you reverse a singly linked list in-place in Python?

Interview Explanation:
"I iterate through the linked list maintaining three pointers: `prev` (initialized to None), `current` (head), and `next_node`.
In each iteration, I store `current.next` in `next_node`, reverse the pointer `current.next = prev`, and advance `prev` and `current`.
Finally, I return `prev` as the new head pointer. This runs in O(n) time and O(1) space."
"""

class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_list(head: ListNode | None) -> str:
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    return " -> ".join(elements)

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:", print_list(head))

    reversed_head = reverse_linked_list(head)
    print("Reversed List:", print_list(reversed_head))
