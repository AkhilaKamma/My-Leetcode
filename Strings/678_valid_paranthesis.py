class Solution:
    def checkValidString(self, s: str) -> bool:

        if len(s) == 1:
            if s == '(' or s == ')':
                return False
            return True

        stack1 = []
        stack2 = []

        for i,char in enumerate(s):
            if char == '(':
                stack1.append(i)
            elif char == "*":
                stack2.append(i)
            else:
                if stack1:
                   stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False

        while stack1 and stack2:

           #compare the indecies for eg: (*)( return False
           #stack[-1] return top element
           if stack1[-1] > stack2[-1]:
               return False
           stack1.pop()
           stack2.pop()

        return stack1 == []
                    

        
