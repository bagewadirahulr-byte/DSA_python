class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Create an empty list to act as our Stack
        stack = []

        # 2. Create a dictionary to map closing brackets to their opening pairs
        bracket_map = {")": "(", "}": "{", "]": "["}

        # 3. Iterate through every character in the string
        for char in s:
            # If the character is a CLOSING bracket...
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the correct opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an OPENING bracket, simply push it onto the stack
                stack.append(char)

        # 4. If the stack is empty at the end, all brackets were matched perfectly!
        return not stack