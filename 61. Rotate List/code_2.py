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
            count = count + 1
        count = count + 1
        # Form a ring
        tail.next = head

        rotate_num = k % count

        curr = head
        prev = tail
        index = 0
        while True:
            if rotate_num == 0:
                prev.next = None
                break

            if count - rotate_num == index:
                prev.next = None
                break
            else:
                prev = curr
                curr = curr.next
                index = index + 1
        return curr