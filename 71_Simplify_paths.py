class Solution:
    def simplifyPath(self, path: str) -> str:
        paths  = path.split('/')
        stack = []
        
        for path in paths:
            if stack and path == '..':
                stack.pop()
            elif path != '.' and path != '..'  and path != '':
                stack.append(path)
                
        return '/' + '/'.join(stack)