class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        for ch in s:
            if ch in ("(", "{", "["):
                stack.append(ch)
            
            else:
                if stack == []:
                    return False

                if ch == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

                elif ch == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False

                elif ch == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        
        if stack == []:
            return True
        return False