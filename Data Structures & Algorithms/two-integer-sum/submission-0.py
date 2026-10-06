class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                j = seen[need]
                return [j, i] if j < i else [i, j]
            seen[x] = i
        return []  # لن نصل لها حسب فرض المسألة