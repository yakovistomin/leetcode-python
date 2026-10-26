class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: set[str] = set()
        left = 0
        result = 0

        for symbol in s:
            while symbol in seen:
                seen.remove(s[left])
                left += 1

            seen.add(symbol)
            result = max(len(seen), result)

        return result
