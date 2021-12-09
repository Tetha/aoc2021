
class BingoBoard:
    def __init__(self, n):
        self.n = n
        self.positions = {}
        self.marks = []
        self.unmarked_numbers = []

    def place_number(self, x, y, num):
        self.positions[num] = (x, y)
        self.unmarked_numbers.append(num)

    def mark_number(self, num):
        if num in self.positions:
            self.marks.append(self.positions[num])
            self.unmarked_numbers.remove(num)

    def score(self):
        return sum(int(n) for n in self.unmarked_numbers)

    def has_complete_row(self):
        for y in range(0, self.n):
            for x in range(0, self.n):
                if (x, y) not in self.marks:
                    break
            else:
                return True

        return False

    def has_complete_column(self):
        for x in range(0, self.n):
            for y in range(0, self.n):
                if (x, y) not in self.marks:
                    break
            else:
                return True

        return False

    def has_complete_diagonal(self):
        for x in range(0, self.n):
            if (x, x) not in self.marks:
                break
        else:
            return True

        for x in range(0, self.n):
            if (x, self.n-x-1) not in self.marks:
                break
        else:
            return True

        return False

    def is_won(self):
        return self.has_complete_column() or self.has_complete_row()
    @classmethod
    def from_lines(klass, n: int, lines: list[str]) -> 'BingoBoard':
        assert len(lines) == n

        for line in lines:
            assert len(line.split()) == n

        result = BingoBoard(n)
        for y, line in enumerate(lines):
            for x, num in enumerate(line.split()):
                result.place_number(x, y, num)
        
        return result
