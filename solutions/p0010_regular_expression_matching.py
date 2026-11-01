import functools


type Rule = tuple[str, bool]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rules = self._make_rules(p)

        @functools.cache
        def _is_match(s_idx: int = 0, r_idx: int = 0) -> bool:
            if r_idx >= len(rules):
                return s_idx >= len(s)

            char, starred = rules[r_idx]

            if not starred:
                if s_idx >= len(s) or char not in ['.', s[s_idx]]:
                    return False
                return _is_match(s_idx + 1, r_idx + 1)

            for consumed in range(len(s) - s_idx + 1):
                if _is_match(s_idx + consumed, r_idx + 1):
                    return True

                if consumed + s_idx >= len(s) or char not in ['.', s[consumed + s_idx]]:
                    return False

            return False

        return _is_match()

    def _make_rules(self, p: str) -> list[Rule]:
        result: list[Rule] = []
        for idx in range(len(p)):
            symbol = p[idx]
            if symbol == '*':
                continue
            rule = (symbol, idx + 1 < len(p) and p[idx + 1] == '*')
            if not rule[1] or not result or result[-1] != rule:
                result.append(rule)
        return result
