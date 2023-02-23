class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expr = []
        curr = 0
        for c in expression:
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                expr.append(curr)
                expr.append(c)
                curr = 0
        expr.append(curr)
        print(expr)
        return self.ways(expr, 0, len(expr) - 1)
    
    def ways(self, expr, start, end):
        if start == end:
            return [expr[start]]
        res = []
        for i in range(start, end + 1):
            item = expr[i]
            if isinstance(item, str):
                left = self.ways(expr, start, i - 1)
                right = self.ways(expr, i + 1, end)
                for l in left:
                    for r in right:
                        if item == "-":
                            res.append(l - r)
                        elif item == "+":
                            res.append(l + r)
                        else:
                            res.append(l * r)
        return res