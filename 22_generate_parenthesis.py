class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recurse(opening, closing, res):
            nonlocal result
            if len(res) == 2 * n:
                result.append(res)
                return
            
            if opening < n:
                recurse(opening + 1, closing, res + "(")
            if opening > closing:
                recurse(opening, closing + 1, res + ")")

        recurse(0, 0, "")
        return result
        