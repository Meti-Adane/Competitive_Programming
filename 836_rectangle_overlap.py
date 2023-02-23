class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        px1, py1, px2, py2 = rec1
        wx1, wy1, wx2, wy2 = rec2
        
        if px2 <= wx1 or wx2 <= px1:
            return False
        
        if py2 <= wy1 or wy2 <= py1:
            return False
        
        return True