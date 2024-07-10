# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None: return
        # find middle of linked list
        prev = ListNode()
        prev.next = head
        slow, fast = head, head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        # reverse from slow to fast
        p = None
        while slow:
            tmp = slow.next
            slow.next = p
            p = slow
            slow = tmp
        
        n1, n2 = head, p
        while n1 and n2:
            tmp1, tmp2 = n1.next, n2.next
            n1.next = n2
            if tmp1 != None: n2.next = tmp1
            n1, n2 = tmp1, tmp2