# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1 and not list2:
            return list1

        dummy = ListNode()
        curr_dummy = dummy
        curr1 = list1
        curr2 = list2

        while curr1 != None or curr2 != None:
            if curr1 == None:
                curr_dummy.next = curr2
                break
            elif curr2 == None:
                curr_dummy.next = curr1
                break

            if curr1.val <= curr2.val:
                curr_dummy.next = curr1
                curr_dummy = curr_dummy.next
                next1 = curr1.next
                curr1.next = None
                curr1 = next1
            else:
                curr_dummy.next = curr2
                curr_dummy = curr_dummy.next
                next2 = curr2.next
                curr2.next = None
                curr2 = next2

        return dummy.next

# O(n) time complexity, O(1) space complexity