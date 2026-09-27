# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        mapping = {}

        count = 0
        while head != None:
            curr = head
            head = head.next
            curr.next = None

            mapping[count] = curr
            count = count + 1

        middle = len(mapping) // 2

        dummy_head = ListNode()
        curr = dummy_head
        for i in range(middle, len(mapping)):
            curr.next = mapping[i]
            curr = curr.next
        curr.next = None

        return dummy_head.next