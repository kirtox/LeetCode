# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        dummy_head = ListNode()
        curr_d = dummy_head
        curr1 = list1
        curr2 = list2

        while curr1 != None or curr2 != None:

            if curr1 == None:
                curr_d.next = curr2
                break
            elif curr2 == None:
                curr_d.next = curr1
                break

            if curr1.val <= curr2.val:
                next1 = curr1.next
                curr_d.next = curr1
                # curr1.next = None
                curr_d = curr_d.next
                curr1 = next1
            else:
                next2 = curr2.next
                curr_d.next = curr2
                # curr2.next = None
                curr_d = curr_d.next
                curr2 = next2
        return dummy_head.next
                