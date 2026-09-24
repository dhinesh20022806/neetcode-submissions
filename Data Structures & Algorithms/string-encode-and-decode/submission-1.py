class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for string in strs:
            res += string + "\n"
        
        return res

    def decode(self, s: str) -> List[str]:

        strs = []
        current_str = ""

        for string in s:
            if string == '\n':
                strs.append(current_str)
                current_str = ""
            else:
                current_str += string
        
        return strs


