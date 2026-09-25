"""
Interview Question: How do you detect a cycle in a linked list using Floyd's Tortoise and Hare algorithm?

Interview Explanation:
"I use two pointers, `slow` moving 1 step at a time, and `fast` moving 2 steps at a time.
If a cycle exists in the linked list, the `fast` pointer will eventually meet the `slow` pointer (`slow == fast`).
If `fast` reaches `None`, the list has no cycle. This operates in O(n) time and O(1) space."
"""

class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print("List has cycle?", has_cycle(node1))
