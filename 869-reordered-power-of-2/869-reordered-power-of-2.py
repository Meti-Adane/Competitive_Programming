class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        hashmap = dict()
        str_num = str(n)
        j = len(str_num)
        count = Counter(str_num)
        
        for i in range(30):
            num = str(2 ** i)
            length = len(num)
            if length not in hashmap:
                hashmap[length] = set()
            hashmap[length].add(num)
          
        
        if j in hashmap:
            for powernumber in hashmap[j]:
                if Counter(powernumber) == count:
                    return True
        return False