class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        num = len(s)
        n = 0
        for i in range(len(t)):
             if n < num and s[n] == t[i]:  # ← guard against empty s
                n += 1
                if n == num:
                    return True
        return n == num  # ← also handles s="" without entering loop
        