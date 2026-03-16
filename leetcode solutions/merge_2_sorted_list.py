class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a "dummy" node. This gives us a convenient starting point.
        dummy = ListNode()

        # 'current' will be the pointer we use to build the new list
        current = dummy

        # 2. Loop as long as BOTH lists still have nodes to compare
        while list1 and list2:
            # Compare the current values of both lists
            if list1.val <= list2.val:
                # If list1 is smaller (or equal), attach it to our merged list
                current.next = list1
                # Move the list1 pointer to its next node
                list1 = list1.next
            else:
                # If list2 is smaller, attach it instead
                current.next = list2
                # Move the list2 pointer forward
                list2 = list2.next

            # Move our building pointer forward so we can attach the next node
            current = current.next

        # 3. Once one list runs out, attach the entire remainder of the OTHER list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # 4. Return the merged list, which starts right after our dummy node
        return dummy.next