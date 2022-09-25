# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.que = []
        self.front = 0
        self.deconstructList(nestedList, self.que)
    
    def next(self) -> int:
        ans= self.que[self.front]
        self.front += 1
        return ans
    
    def hasNext(self) -> bool:
        if self.front >= len(self.que):
            return False
        return True
    
    def deconstructList(self, arr, output):
        for val in arr:
            if not val.isInteger():
                self.deconstructList(val.getList(), output)
            else:
                output.append(val)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())