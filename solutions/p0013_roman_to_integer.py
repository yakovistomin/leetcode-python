ROMAN_INT_MAP = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for cur_synbol, next_symbol in zip(s, [*s[1:], None], strict=True):
            value = ROMAN_INT_MAP[cur_synbol]
            if next_symbol and value < ROMAN_INT_MAP[next_symbol]:
                result -= value
            else:
                result += value
        return result
