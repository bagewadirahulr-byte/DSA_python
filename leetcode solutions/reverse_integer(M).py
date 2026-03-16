class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit integer limits
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1

        # Determine the sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        while x != 0:
            # Pop the last digit
            digit = x % 10
            x //= 10

            # Update the reversed number
            reversed_num = (reversed_num * 10) + digit

        # Apply the sign
        result = sign * reversed_num

        # Overflow check
        if result < MIN_INT or result > MAX_INT:
            return 0

        return result