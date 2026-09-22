class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        node = dummy 

        while list1 and list2:

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else: 
                node.next = list2
                list2 = list2.next

            # Move node forward
            node = node.next

        # One list is empty.
        # Attach whatever is left from the other list.
        node.next = list1 or list2

        # Return the beginning of the real list.
        return dummy.next
        