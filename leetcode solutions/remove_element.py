class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 'k' is our "slow" pointer. It keeps track of where to place
        # the next element that is NOT equal to 'val'.
        k = 0

        # 'i' is our "fast" pointer that scans through every item in the array.
        for i in range(len(nums)):
            # If the current number is NOT the value we want to remove...
            if nums[i] != val:
                # ...we copy it to the 'k' position...
                nums[k] = nums[i]
                # ...and step 'k' forward to get ready for the next valid number.
                k += 1

        # 'k' now represents the total number of elements that are not 'val'
        return k