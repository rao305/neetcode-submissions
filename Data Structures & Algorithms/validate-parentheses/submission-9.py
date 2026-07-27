class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for items in s:
            if items in pairs:
                stack.append(items)
            else:
                if not stack or pairs[stack[-1]] != items:
                    return False
                stack.pop()
        return not stack
                

        