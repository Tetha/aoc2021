
from dataclasses import dataclass


@dataclass
class LineSegment:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_axis_aligned(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def intersects_with(self, other):
        if self.x1 == self.x2:
            return other.y1 <= self.y1 <= other.y2 or other.y1 <= self.y2 <= other.y2
        else:
            assert self.y1 == self.y2
            return other.x1 <= self.x1 <= other.x2 or other.x1 <= self.x2 <= other.x2

def parse_line_segment_line(line: str) -> LineSegment:
    line_parts = line.split(" -> ")
    assert len(line_parts) == 2
    coord1, coord2 = line_parts[0], line_parts[1]

    coord1_parts = coord1.split(",")
    coord2_parts = coord2.split(",")

    assert len(coord1_parts) == 2
    assert len(coord2_parts) == 2

    x1, y1 = int(coord1_parts[0]), int(coord1_parts[1])
    x2, y2 = int(coord2_parts[0]), int(coord2_parts[1])

    return LineSegment(x1, y1, x2, y2)