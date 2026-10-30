Rule = tuple[str, bool]


class Solution:
    def isMatch(self, value: str, expression: str) -> bool:
        rules = self._make_rules(expression)
        return self._apply_rules(value=value, rules=rules, equals_count=0)[0]

    def _make_rules(self, p: str) -> list[Rule]:
        result: list[Rule] = []
        for idx, symbol in enumerate(p):
            if symbol == '*':
                continue
            rule = (symbol, idx + 1 < len(p) and p[idx + 1] == '*')
            if result and rule[1] and result[-1] == rule:
                continue
            result.append(rule)
        return result

    def _apply_rules(self, value: str, rules: list[Rule], equals_count: int) -> tuple[bool, int]:
        if not value and not rules:
            return True, equals_count
        if value and not rules:
            return False, equals_count

        current_rule = rules[0]
        if not value and not current_rule[1]:
            return False, equals_count
        if not value:
            return self._apply_rules(value, rules[1:], equals_count)

        if not current_rule[1]:
            return self._apply_single_rule(
                value=value,
                rules=rules,
                current_rule=current_rule,
                equals_count=equals_count,
            )

        return self._apply_multiple_rule(
            value=value,
            rules=rules,
            current_rule=current_rule,
            equals_count=equals_count,
        )

    def _apply_single_rule(
        self,
        value: str,
        rules: list[Rule],
        current_rule: Rule,
        equals_count: int,
    ) -> tuple[bool, int]:
        equals_count += 1
        if current_rule[0] == '.' or current_rule[0] == value[0]:
            if len(rules) == 1:
                return len(value) == 1, equals_count
            return self._apply_rules(value[1:], rules[1:], equals_count)
        return False, equals_count

    def _apply_multiple_rule(
        self,
        value: str,
        rules: list[Rule],
        current_rule: Rule,
        equals_count: int,
    ) -> tuple[bool, int]:
        idx = 1
        while True:
            result, iteration_equals_count = self._apply_rules(value=value[idx - 1 :], rules=rules[1:], equals_count=0)
            if result:
                return True, equals_count + iteration_equals_count

            if current_rule[0] != '.' and value[idx - 1] != current_rule[0]:
                return False, equals_count + iteration_equals_count

            if idx >= len(value):
                if iteration_equals_count > 0:
                    return False, equals_count + iteration_equals_count
                return current_rule[0] == '.' or value[idx - 1] == current_rule[
                    0
                ], equals_count + iteration_equals_count

            idx += 1
