# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 0 or not head:
            return head

        mapping = {}

        count = 0
        while head != None:
            curr = head
            head = head.next
            curr.next = None
            
            mapping[count] = curr
            count = count + 1

        rotate_num = k % len(mapping)

        # Seq
        rotate_ind = [x for x in range(len(mapping))]
        rotate_ind = rotate_ind[-rotate_num:] + rotate_ind[:-rotate_num]

        dummy_head = ListNode()
        curr = dummy_head
        for ind in rotate_ind:
            curr.next = mapping[ind]
            curr = curr.next
        curr.next = None

        return dummy_head.next