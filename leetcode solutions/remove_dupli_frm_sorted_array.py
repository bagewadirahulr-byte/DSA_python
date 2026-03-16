class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: If the list is empty, return 0
        if not nums:
            return 0

        # 'i' is our "slow" pointer. It keeps track of where to place
        # the next unique element we find.
        i = 0

        # 'j' is our "fast" pointer. It scans through the array
        # starting from the second element (index 1).
        for j in range(1, len(nums)):
            # If we find a number that is DIFFERENT from the last unique number...
            if nums[j] != nums[i]:
                # ...we step 'i' forward by one...
                i += 1
                # ...and copy the new unique number into that spot.
                nums[i] = nums[j]

        # Since 'i' is an index (starting at 0), the total count of
        # unique elements is 'i + 1'.
        return i + 1