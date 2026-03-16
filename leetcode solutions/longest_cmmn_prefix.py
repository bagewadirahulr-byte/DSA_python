class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # If the list is empty, there is no common prefix
        if not strs:
            return ""

        # 1. Start by assuming the very first string is the entire common prefix
        prefix = strs[0]

        # 2. Loop through the rest of the strings in the list
        for s in strs[1:]:
            # 3. While the current string does NOT start with our assumed prefix...
            while not s.startswith(prefix):
                # ...chop off the last letter of our prefix and try again
                prefix = prefix[:-1]

                # If we chop off all the letters, they have nothing in common
                if not prefix:
                    return ""

        # 4. Once we've checked all strings, whatever is left is the longest prefix
        return prefix