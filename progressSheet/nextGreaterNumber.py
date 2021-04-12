# question url : https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temprature_queue = []
        output = [0] * len(T)
        index = 0

        for pos, temprature in enumerate(T):
            if not len(temprature_queue):
                temprature_queue.append((temprature, pos))

            elif len(temprature_queue) and temprature <= temprature_queue[-1][0]:
                temprature_queue.append((temprature, pos))
            else:
                while len(temprature_queue) and temprature > temprature_queue[-1][0]:
                    topElement = temprature_queue.pop()
                    output[topElement[1]] = pos - topElement[1]
                temprature_queue.append((temprature, pos))

        return output