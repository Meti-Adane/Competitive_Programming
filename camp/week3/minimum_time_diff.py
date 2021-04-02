# question url : https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        totalMinutes = []
        minDiff = float("inf")

        for time in timePoints:
            totalMinutes.append(self.getMinutes(time))

        totalMinutes.sort()

        for slowPointer in range(len(totalMinutes) - 1):
            fastPointer = slowPointer + 1
            minDiff = self.getDiff(minDiff, fastPointer, slowPointer, totalMinutes)

        minDiff = self.getDiff(minDiff, -1, 0, totalMinutes)
        return minDiff

    def getMinutes(self, timeString):
        hour, minute = timeString.split(":")
        if hour == "00":
            hour = "24"
        return (int(hour) * 60) + int(minute)

    def getDiff(self, minDiff, fast, slow, arr):
        diff = (arr[fast] - arr[slow])

        if diff > 720:
            diff -= 1440

        return min(minDiff, abs(diff))
