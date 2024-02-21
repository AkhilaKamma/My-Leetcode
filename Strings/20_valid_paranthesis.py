class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            
            else:

                if len(stack) > 0:
                    match_char = stack.pop()
                    if match_char != '(' and char == ')':
                        return False
                    elif match_char != '{' and char == '}':
                        return False
                    elif match_char != '[' and char == ']':
                        return False   
                    else:
                        continue
                else:
                    return False
                    
        if len(stack) > 0:
            return False
            
        return True
