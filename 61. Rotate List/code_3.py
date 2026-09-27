# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 0:
            return head

        tail = head
        count = 0

        while tail.next != None:
            tail = tail.next
            count += 1
        count += 1

        # Early return if rotate_num == 0 -> Not need to process.
        rotate_num = k % count
        if rotate_num == 0:
            return head

        # Form a ring
        tail.next = head

        curr = head
        prev = tail
        for i in range(count - rotate_num):
            prev = curr
            curr = curr.next
        prev.next = None
        return curr