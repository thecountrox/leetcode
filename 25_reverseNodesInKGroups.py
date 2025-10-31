class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reverse(head,k): 
# recursive reverse function
    temp = head
    prev = None
    count = 0
    while count <= k:
        nextNode = temp.next
        temp.next = prev
        prev = temp
        temp = nextNode
        count+=1
    return prev

m = ListNode(1)
m.next = ListNode(2)
m.next.next = ListNode(3)
m.next.next.next = ListNode(4)
m.next.next.next.next = ListNode(5)
print(m.next.next.next.next.val)
m = reverse(m,3)
print(m.val)
