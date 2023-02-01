class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = count = flips = 0
        minflips = len(blocks)

        for right in range(len(blocks)):
            if count == k:
                minflips = min(flips, minflips)
            if blocks[right] == "W":
                flips += 1
            count += 1
            
            while left < right and count > k:
                if blocks[left] == 'W':
                    flips -= 1
                count -= 1
                left += 1
        return min(minflips, flips)