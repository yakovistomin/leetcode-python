class IndexSolution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s

        result = []
        step = 2 * num_rows - 2

        for row in range(num_rows):
            for step_idx in range(row, len(s), step):
                result.append(s[step_idx])
                diag_idx = step_idx + step - row * 2
                if 0 < row < num_rows - 1 and diag_idx < len(s):
                    result.append(s[diag_idx])

        return ''.join(result)


class SimulationSolution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s

        rows: list[list[str]] = [[] for _ in range(num_rows)]
        row = 0
        step = 1

        for symbol in s:
            rows[row].append(symbol)
            if row == 0:
                step = 1
            elif row == num_rows - 1:
                step = -1
            row += step

        return ''.join(''.join(row) for row in rows)


Solution = IndexSolution
