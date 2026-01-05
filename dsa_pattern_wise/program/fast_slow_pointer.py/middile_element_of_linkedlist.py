class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def middleNode(head: ListNode) -> ListNode:
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def create_linked_list(arr):
    head = ListNode(arr[0])
    curr=head
    for val in arr[1:]:
        curr.next=ListNode(val)
        curr=curr.next
    return head

head= create_linked_list([2,3,4,5,6])
mid=middleNode(head)

print(mid.val)