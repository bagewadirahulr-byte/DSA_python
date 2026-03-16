# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the head swap
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            # Nodes to be swapped
            first = curr
            second = curr.next

            # Record the node after the pair
            next_pair = second.next

            # Swapping
            second.next = first
            first.next = next_pair
            prev.next = second

            # Move pointers forward for the next pair
            prev = first
            curr = next_pair

        return dummy.next