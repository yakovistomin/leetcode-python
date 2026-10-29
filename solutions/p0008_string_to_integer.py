import string


INT_MAX = 2_147_483_647
INT_MIN = -2_147_483_648
MAX_INT_DIV_10 = INT_MAX // 10
MAX_LAST_NEGATIVE_DIGIT = 8
MAX_LAST_DIGIT = 7
SYMBOL_MAP = {symbol: idx for idx, symbol in enumerate(string.digits)}


class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1

        sign = 1
        if idx < len(s) and s[idx] in '-+':
            sign = -1 if s[idx] == '-' else 1
            idx += 1

        result = 0

        while idx < len(s) and s[idx] in SYMBOL_MAP:
            digit = SYMBOL_MAP[s[idx]]

            if result > MAX_INT_DIV_10 or (result == MAX_INT_DIV_10 and digit > MAX_LAST_DIGIT):
                return INT_MAX
            if result < -MAX_INT_DIV_10 or (result == -MAX_INT_DIV_10 and digit > MAX_LAST_NEGATIVE_DIGIT):
                return INT_MIN

            result = result * 10 + digit * sign

            idx += 1

        return result
