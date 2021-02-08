class Solution:
    def __init__(self):
        self.container = []

    def isValid(self, s: str) -> bool:
        opening_parentheses = ["(", "[", "{"]
        closing_parentheses = [")", "]", "}"]

        if len(s) % 2 != 0: return False

        i = 0
        p = 0
        while i < len(s):
            if s[i] in opening_parentheses:
                self.push(s[i])
            elif s[i] in closing_parentheses:
                p += 1
                # n = opening_parentheses.index(self.peek())
                if (self.isEmpty() == False) and (s[i] == closing_parentheses[opening_parentheses.index(self.peek())]):
                    self.pop()
                    p -= 1
            i = i + 1
        # print(self.container, self.isEmpty(), self.peek())
        if self.isEmpty() and p == 0:
            return True
        else:
            return False

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0


closing = [")", "]", "}"]
print(closing.index("}"))