# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev, curr = None, head
        # Keep going until curr reaches the end (None)
        while curr:

            # Save the next node before we change curr.next
            # Example: if curr is 1, temp saves 2
            temp = curr.next

            # Reverse the arrow
            # Instead of curr pointing forward, make it point backward to prev
            # Example: 1 → 2 becomes 1 → None
            curr.next = prev

            # Move prev forward to the current node
            # Example: prev now points to 1
            prev = curr

            # Move curr forward to the node we saved
            # Example: curr now points to 2
            curr = temp

        # prev is now pointing to the first node of the reversed list
        # Example: 3 → 2 → 1 → None
        return prev