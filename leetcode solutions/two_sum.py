class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the numbers we've seen and their indices.
        # Format will be {number: index}
        seen_numbers = {}

        # Iterate through the array using enumerate to get both index (i) and value (num)
        for i, num in enumerate(nums):
            # Calculate the number we need to find to reach the target
            complement = target - num

            # Check if we have already seen this complement
            if complement in seen_numbers:
                # If yes, return the index of the complement and the current index
                return [seen_numbers[complement], i]

            # If not, add the current number and its index to our dictionary
            seen_numbers[num] = i
            # 1. Create an instance of the Solution class
            sol = Solution()

            # 2. Call the method with sample data
            result = sol.twoSum([2, 7, 11, 15], 9)

            # 3. Print the result so it shows up in your terminal
            print(result)
