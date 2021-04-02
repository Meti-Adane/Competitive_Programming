# question url : https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leaders = [i for i in range(26)]
        size = [1 for _ in range(26)]

        def find(a):
            if leaders[a] == a:
                return leaders[a]
            leaders[a] = find(leaders[a])
            return leaders[a]

        def union(a, b):
            leader_of_a = find(a)
            leader_of_b = find(b)

            if size[leader_of_a] >= size[leader_of_b]:
                leaders[leader_of_b] = leader_of_a
                size[leader_of_b] += 1
            else:
                leaders[leader_of_a] = leader_of_b
                size[leader_of_a] += 1

        for eq in equations:
            if eq[1] == "=":
                index1 = ord(eq[0]) - ord('a')
                index2 = ord(eq[-1]) - ord('a')
                union(index1, index2)

        for eq in equations:
            if eq[1] == "!":

                index1 = ord(eq[0]) - ord('a')
                index2 = ord(eq[-1]) - ord('a')
                if find(index1) == find(index2):
                    return False

        return True



