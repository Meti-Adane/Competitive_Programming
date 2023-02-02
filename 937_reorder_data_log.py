class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        heap, digit_logs, ans = [], [], []
        
        for i, log in enumerate(logs):
            splitted = log.split(' ')
            if splitted[1].isdigit():
                digit_logs.append(log)
            else:
                letters = " ".join(splitted[1:])
                heappush(heap, (letters, splitted[0]))
        
        while heap:
            content, id = heappop(heap)
            ans.append(id+ " " +content)
        return ans + digit_logs