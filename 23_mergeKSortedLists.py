class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        res = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                heapq.heappush(q, temp.val)
                temp = temp.next

        head1 = ListNode()
        head = head1
        for i in range(len(q)):
            # res.append(heapq.heappop(q))

            head.next = ListNode(heapq.heappop(q))
            head = head.next
        return head1.next
