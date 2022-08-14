

from .line_segment import LineSegment, parse_line_segment_line


def test_linesegment_intersection():
    assert LineSegment(x1=1, y1=12, x2=1, y2=24).is_axis_aligned()
    assert LineSegment(x1=12, y1=1, x2=24, y2=1).is_axis_aligned()
    assert not LineSegment(x1=12, y1=1, x2=24, y2=2).is_axis_aligned()


def test_intersection():
    l1 = LineSegment(x1=1, y1=1, x2=1, y2=3)
    l2 = LineSegment(x1=1, y1=1, x2=3, y2=1)

    assert l1.intersects_with(l2)

    l3 = LineSegment(x1=1, y1=1, x2=1, y2=3)
    l4 = LineSegment(x1=5, y1=1, x2=5, y2=3)
    assert not l3.intersects_with(l4)

def test_parse_line_segment_line() -> None:
    line = "6,4 -> 2,0"
    segment = parse_line_segment_line(line)
    assert segment == LineSegment(x1=6, y1=4, x2=2, y2=0)

