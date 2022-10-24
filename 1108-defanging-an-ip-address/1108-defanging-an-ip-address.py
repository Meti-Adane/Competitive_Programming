class Solution:
    def defangIPaddr(self, address: str) -> str:
        ipaddress = list(address)
        for i, ip in enumerate(ipaddress):
            if ip == '.':
                ipaddress[i] = "[.]"
        return "".join(ipaddress)