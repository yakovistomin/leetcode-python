import math


class ReverseHalfSolution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or not x % 10:
            return False

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return x == reversed_x or x == reversed_x // 10


class CompareEndsSolution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or not x % 10:
            return False

        len_x = math.floor(math.log10(x))

        while len_x > 0:
            right_digit = x % 10
            left_digit = (x // 10**len_x) % 10
            if right_digit != left_digit:
                return False
            x = x // 10
            len_x -= 2

        return True


Solution = ReverseHalfSolution
