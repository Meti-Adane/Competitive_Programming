class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1Arr = []
        img2Arr = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    img1Arr.append((i,j))
                if img2[i][j] == 1:
                    img2Arr.append((i,j))
        container = {}
        ans = 0
        for a_x, a_y in img1Arr:
            for b_x,b_y in  img2Arr:
                point = (b_x - a_x, b_y - a_y)
                container[point] = container.get(point, 0) + 1
                ans = max(ans, container[point])
        return ans