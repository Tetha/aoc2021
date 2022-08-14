
from .bingo_board import BingoBoard


def test_row_completed():
    subject = BingoBoard.from_lines(3, [
        '1 2 3',
        '4 5 6',
        '7 8 9',
    ])

    assert not subject.has_complete_row()
    subject.mark_number('1')
    assert not subject.has_complete_row()
    subject.mark_number('2')
    assert not subject.has_complete_row()
    subject.mark_number('3')
    assert subject.has_complete_row()

def test_column_completed():
    subject = BingoBoard.from_lines(3, [
        '1 2 3',
        '4 5 6',
        '7 8 9',
    ])

    assert not subject.has_complete_column()
    subject.mark_number('1')
    assert not subject.has_complete_column()
    subject.mark_number('4')
    assert not subject.has_complete_column()
    subject.mark_number('7')
    assert subject.has_complete_column()

def test_rising_diagonal_completed():
    subject = BingoBoard.from_lines(3, [
        '1 2 3',
        '4 5 6',
        '7 8 9',
    ])

    assert not subject.has_complete_diagonal()
    subject.mark_number('7')
    assert not subject.has_complete_diagonal()
    subject.mark_number('5')
    assert not subject.has_complete_diagonal()
    subject.mark_number('3')
    assert subject.has_complete_diagonal()


def test_falling_diagonal_completed():
    subject = BingoBoard.from_lines(3, [
        '1 2 3',
        '4 5 6',
        '7 8 9',
    ])

    assert not subject.has_complete_diagonal()
    subject.mark_number('1')
    assert not subject.has_complete_diagonal()
    subject.mark_number('5')
    assert not subject.has_complete_diagonal()
    subject.mark_number('9')
    assert subject.has_complete_diagonal()

def test_sample():
    subject = BingoBoard.from_lines(5, [
        '14 21 17 24  4',
        '10 16 15  9 19',
        '18  8 23 26 20',
        '22 11 13  6  5',
        ' 2  0 12  3  7',
    ])

    for num in [
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    ]:
        subject.mark_number(str(num))
        if subject.is_won():
            break

    assert subject.score() == 188