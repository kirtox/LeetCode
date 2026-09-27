# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        dummy_head = ListNode()
        curr = head
        prev = None
        while curr != None:
            dummy_head.next = curr
            curr = curr.next
            dummy_head.next.next = prev
            prev = dummy_head.next
        return dummy_head.next