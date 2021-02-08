import math
class Solution:
    def evalRPN(self, tokens) -> int:
        operands = []
        for i in tokens:

            if i.lstrip('-').isdigit():
                operands.append(i)
                pass
            elif len(operands) > 1:
                a = operands.pop()
                b = operands.pop()
                operands.append(self.calc(int(a), int(b), i))
        return operands[-1]

    def calc(self, a, b, operator):
        if operator == "/":
            if b == 0:
                return 0
            res = b / a
            if res < 0:
                return math.ceil(res)
            return b // a
        if operator == "*":
            return a * b
        if operator == "+":
            return a + b
        if operator == "-":
            return b - a



