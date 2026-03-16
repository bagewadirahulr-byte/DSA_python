class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Negative numbers are never palindromes (e.g., -121 reversed is 121-)
        if x < 0:
            return False

        # 2. Store the original number so we can compare it at the end
        original = x
        reversed_num = 0

        # 3. Mathematically reverse the number
        while x > 0:
            # Get the last digit of x
            last_digit = x % 10

            # Shift the currently reversed number to the left by 1 digit,
            # then add the new last digit
            reversed_num = (reversed_num * 10) + last_digit

            # Remove the last digit from x
            x = x // 10

            # 4. Check if the reversed number matches the original
        return original == reversed_num