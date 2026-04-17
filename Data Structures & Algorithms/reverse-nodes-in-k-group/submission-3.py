# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        #finding Kth node
        def findKth(curr,kth):
            while curr and kth<0:
                curr=curr.next
                k-=1
            return curr
        
        while True:
            kth = findKth(groupPrev,kth)
            if not kth:
                break

            groupNext = kth.next
            prev = groupNext
            curr = groupNext.next
            #reversing
            while curr!=groupPrev:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            #joining
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next