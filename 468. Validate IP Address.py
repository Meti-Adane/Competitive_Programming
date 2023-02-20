class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        hasdot = True if '.' in queryIP else False
        digits = {str(i) for i in range(10)}
        chars = {chr(i) for i in range(97, 103)}
        def validateIPV4(s):
            arr = s.split('.')
            if len(arr) != 4:
                return False
            
            for x in arr:
                if (len(x) >= 2 and x[0] == '0'):
                    return False
                for char in x:
                    if char not in digits:
                        print(x)
                        return False
                if not x or int(x) > 255:
                    return False
                
            return True
        
        def validateIPV6(s):
            arr = s.split(':')
            if len(arr) != 8:
                return False
            
            for x in arr:
                if len(x) > 4 or len(x) == 0:
                    return False
                for char in x:
                    if not (char in digits or char.lower() in chars):
                        return False
            return True
        
        if hasdot:
            return "IPv4" if validateIPV4(queryIP) else "Neither"
        return "IPv6" if validateIPV6(queryIP) else "Neither"