class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num != 0:
                visited.add(num)
        return len(visited)