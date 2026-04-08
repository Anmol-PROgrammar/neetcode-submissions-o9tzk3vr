class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        if len(s) <= 1:
            return False 
        stack.append(s[i])
        i+=1
        while i < len(s):
            if  s[i] == ')' or s[i] == ']' or s[i] == '}':
                #check stack last element
                if len(stack) and (self.validBracket(stack[-1]) == s[i]):
                    stack.pop()
                else:
                     return False
            elif  s[i] == '(' or s[i] == '[' or s[i] == '{':
               #add in the stack for all opening bracket
                stack.append(s[i])
            i += 1
        return len(stack) == 0

            


    def validBracket(self, bracket) -> str:
        if bracket == '(':
            return ')'
        elif bracket == '[':
            return ']'
        elif bracket == '{':
            return '}'
            