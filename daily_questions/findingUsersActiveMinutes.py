# question url: https://leetcode.com/problems/


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userUniqueMinutes = {}
        output = [0] * k

        for id, minute in (logs):
            if userUniqueMinutes.get(id):
                userUniqueMinutes[id].add(minute)
            else:
                userUniqueMinutes[id] = {minute}

        for id in userUniqueMinutes.keys():
            uam = len(userUniqueMinutes[id])
            output[uam - 1] += 1
        return output