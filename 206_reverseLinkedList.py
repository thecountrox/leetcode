# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: ListNode) -> ListNode:
    if head is None:
        return head
    prev = None
    temp = head
    nextNode = head.next
    while nextNode:
        temp = nextNode
        nextNode = temp.next
        temp.next = prev
        prev = temp
    return head
            
