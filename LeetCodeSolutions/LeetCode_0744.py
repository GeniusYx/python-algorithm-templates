class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]
