# question url: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxDepth = [0]
        heapq.heapify(maxDepth)
        if not root:
            return 0
        self.findMax(root, maxDepth)
        return heapq.heappop(maxDepth) + 1

    def findMax(self, root, maxDepth, depth=0):
        temp = root
        depth += 1
        for child in temp.children:
            if depth > maxDepth[0]:
                heapq.heappop(maxDepth)
                heapq.heappush(maxDepth, depth)

                self.findMax(child, maxDepth, depth)