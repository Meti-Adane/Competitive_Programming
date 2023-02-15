class Solution:
    def checkValidString(self, s):
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack1.append(i)
            elif s[i]== '*':
                stack2.append(i)
            else:
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
            print(stack1, stack2)
        print(stack1, stack2)
        while stack1:
            
            if len(stack2)==0:
                return False
            
            elif stack1[-1]< stack2[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False
        return True