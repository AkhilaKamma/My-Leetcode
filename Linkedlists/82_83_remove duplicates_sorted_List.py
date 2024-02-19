#82......
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

#83......

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(None, None)
        dummy.next = head
        
        left = dummy
        
        right = head

        while right and right.next:

            if right.val == right.next.val:
            
                while right.next and right.val == right.next.val:
                    right = right.next

                right.next, right = None, right.next
                left.next = right
        
            else:
                left = right
                right = right.next

        return dummy.next
        

        
