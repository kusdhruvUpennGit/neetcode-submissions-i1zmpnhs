# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grpPrev = dummy

        def getKth(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr
        
        while True:
            kth = getKth(grPprev,k)
            if not kth:
                break
            
            grpNxt = kth.next
            prev = grpNxt
            curr = grpNxt.next

            # Reverse
            while curr!=grpNxt:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # Joining
            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp
        return dummy.next