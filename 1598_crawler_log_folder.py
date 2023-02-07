class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operation = 0
        for i in logs:
            if i == "./":
                continue
            elif i == "../":
                if operation > 0:
                    operation -= 1
            else:
                operation += 1
        return operation 
       
        