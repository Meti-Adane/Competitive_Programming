# question url : https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution:
    def searchBST(self, root, val: int):
        temp = root
        while temp:
            if val > temp.val:
                temp = temp.right
            elif val < temp.val:
                temp = temp.left
            else:
                return temp
