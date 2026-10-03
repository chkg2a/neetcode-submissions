class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashStack = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for c in s:
            if c == ")" or c == "]" or c == "}":
                if len(stack) == 0 or hashStack[c] != stack[-1]:
                    return False
                if hashStack[c] == stack[-1]:
                    stack.pop()
            else:
                stack.append(c)
        print(stack)
        
        return len(stack) == 0