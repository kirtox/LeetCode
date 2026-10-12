/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr and list2 == nullptr){
            return list1;
        }

        ListNode* dummy = new ListNode();
        ListNode* curr_dummy = dummy;
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;
        ListNode* next1;
        ListNode* next2;

        while (curr1 != nullptr or curr2 != nullptr){
            if (curr1 == nullptr){
                curr_dummy->next = curr2;
                break;
            } else if (curr2 == nullptr){
                curr_dummy->next = curr1;
                break;
            }

            if (curr1->val <= curr2->val){
                curr_dummy->next = curr1;
                curr_dummy = curr_dummy->next;
                next1 = curr1->next;
                curr1->next = nullptr;
                curr1 = next1;
            } else {
                curr_dummy->next = curr2;
                curr_dummy = curr_dummy->next;
                next2 = curr2->next;
                curr2->next = nullptr;
                curr2 = next2;
            }
        }

        return dummy->next;
    }
};

// O(n) time complexity, O(1) space complexity