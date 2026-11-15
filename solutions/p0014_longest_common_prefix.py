class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = []
        max_len = 0
        for s in strs:
            max_len = max(max_len, len(s))

        for idx in range(max_len):
            cur_result = set()
            for s in strs:
                cur_result.add(s[idx] if len(s) > idx else None)
            if len(cur_result) > 1:
                break
            result.append(str(cur_result.pop()))

        return ''.join(result)
