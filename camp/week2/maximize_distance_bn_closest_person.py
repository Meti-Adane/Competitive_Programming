class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        spaces = []
        slow = 0

        if len(seats) == 2:
            return 1

        for i in range(1, len(seats) - 1):
            fast = seats[i]
            while fast != 1 and i < len(seats) - 1:
                i += 1
                fast = seats[i]

            if seats[0] == slow == 0 and fast == 1:
                spaces.append(i)
                slow = i
            if i != slow and fast == seats[slow]:
                sitAtIndex = (i - slow) // 2
                diff = i - (i - sitAtIndex)

                spaces.append((diff))
                slow = i

        if fast == 0:
            spaces.append((len(seats) - slow - 1))
        spaces.sort()
        return spaces[-1]