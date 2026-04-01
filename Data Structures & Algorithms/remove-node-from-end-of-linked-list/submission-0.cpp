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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *prev;
        ListNode* temp = head;
        int count = 0;
        while(temp != nullptr)
        {
            temp = temp->next;
            count++;
        }

        int var = (count - n); // from begin
        cout<<var;
        
        temp = head;
        prev = nullptr;
        while(var!=0)
        {
            var--;
            prev = temp;
            temp = temp->next;       
            cout<<temp->val;     
        }

        if(prev == nullptr)
        {
            return head->next;
        }
        else
        {
            prev->next = temp->next;
        }
        return head;
        
    }
};
