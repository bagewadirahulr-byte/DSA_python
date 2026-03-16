class Solution:
    def intToRoman(self, num: int) -> str:
        # List of Roman numeral symbols and their values (including subtractive cases)
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        res = ""

        for value, symbol in roman_map:
            if num == 0:
                break

            # Determine how many times this symbol fits
            count = num // value
            res += (symbol * count)

            # Update num to the remainder
            num %= value

        return res