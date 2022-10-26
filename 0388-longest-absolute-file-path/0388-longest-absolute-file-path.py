class Solution:
    def lengthLongestPath(self, s: str) -> int:
        levels = dict({-1:[-1]})
        lines = s.splitlines()
        ans = 0 
        
        for line in lines:
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            size = levels[depth-1][-1] + 1 + len(name) #parsize + 1 '\' + currname
            if '.' in name:
                ans = max(ans, size)
            else:
                levels[depth] = levels.get(depth, []) + [size]
        return ans