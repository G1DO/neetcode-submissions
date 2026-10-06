class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)           # مفتاح جديد → يعمل list فاضية تلقائيًا
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)   # آمن
        return list(res.values())         # رجّع list مش view