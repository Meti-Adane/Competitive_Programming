class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha(): #handle email
            at = s.find('@')
            return (s[0].lower()+
                    '*****'+s[at-1].lower()+ '@'+
                    "".join([s[i].lower() for i in range(at+1, len(s))])
                    )
        digits= re.findall('[0-9]', s)
        return (["", "+*-", "+**-", "+***-"][len(digits)%10]) + "***-***-" + "".join(digits[-4:])