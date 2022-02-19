class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter1 = Counter(s)
        counter2 = Counter(t)
        steps = 0
        
        for letter, freq in counter1.items():
            if letter not in counter2:
                steps += freq
            elif counter1[letter] > counter2[letter]:
                steps += counter1[letter] - counter2[letter]
        
        return steps 