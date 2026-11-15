ROMAN_INT_MAP = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
)
MAX_REPEATABLE_CHARACTERS = 4


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []

        for symbol, value in ROMAN_INT_MAP:
            count, num = divmod(num, value)
            if count > 0:
                result.append(symbol * count)

        return ''.join(result)
