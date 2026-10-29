MAX_INT_DIV_10 = 214_748_364
MIN_LAST_DIGIT = -8
MAX_LAST_DIGIT = 7


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        result = 0

        while x != 0:
            digit = x % 10
            if is_negative and digit:
                digit -= 10

            x = (x - digit) // 10

            if is_negative:
                if result < -MAX_INT_DIV_10 or (result == -MAX_INT_DIV_10 and digit < MIN_LAST_DIGIT):
                    return 0
            elif not is_negative and (result > MAX_INT_DIV_10 or (result == MAX_INT_DIV_10 and digit > MAX_LAST_DIGIT)):
                return 0

            result = result * 10 + digit

        return result
