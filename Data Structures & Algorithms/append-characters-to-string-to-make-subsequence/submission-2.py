class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_number=len(t)
        s_number=len(s)
        t_counter = 0
        
        t_remaining= t_number
        for i in range(s_number):
            if (t[t_counter]==s[i]):
                t_counter = t_counter+1
                t_remaining = t_remaining -1
                if t_remaining == 0:
                    return 0
        return t_remaining


        