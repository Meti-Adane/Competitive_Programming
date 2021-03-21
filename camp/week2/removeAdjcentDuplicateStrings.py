# questionurl: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, S: str) -> str:
        container = []
        for char in S:
            if container and char == container[-1]:
                container.pop()
            else:
                container.append(char)
        return "".join(container)