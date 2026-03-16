class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Create a dictionary to map Roman numerals to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        # 2. Iterate through the string, character by character
        for i in range(n):
            # 3. Check for the subtraction rule:
            # If we are not at the last character AND the current symbol's value
            # is less than the next symbol's value...
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                # ...we subtract the current value from the total
                total -= roman_map[s[i]]
            else:
                # ...otherwise, we just add it to the total
                total += roman_map[s[i]]

        return total