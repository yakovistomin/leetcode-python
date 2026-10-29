import string


INT_MAX = 2_147_483_647
INT_MIN = -2_147_483_648
MAX_INT_DIV_10 = INT_MAX // 10
MAX_LAST_NEGATIVE_DIGIT = 8
MAX_LAST_DIGIT = 7
SYMBOL_MAP = {symbol: idx for idx, symbol in enumerate(string.digits)}


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')

        sign = 1
        start = 0
        if s and s[0] in '-+':
            sign = -1 if s[0] == '-' else 1
            start = 1

        result = 0
        for symbol in s[start:]:
            if symbol not in SYMBOL_MAP:
                break

            digit = SYMBOL_MAP[symbol]

            if result > MAX_INT_DIV_10 or (result == MAX_INT_DIV_10 and digit > MAX_LAST_DIGIT):
                return INT_MAX
            if result < -MAX_INT_DIV_10 or (result == -MAX_INT_DIV_10 and digit > MAX_LAST_NEGATIVE_DIGIT):
                return INT_MIN

            result = result * 10 + digit * sign

        return result
