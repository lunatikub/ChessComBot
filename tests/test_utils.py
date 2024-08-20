from utils import parse_move


def test_parse__move():

    from_square, to_square = parse_move("e2e4")
    assert from_square == "e2" and to_square == "e4"

    from_square, to_square = parse_move("Ke2-e4")
    assert from_square == "e2" and to_square == "e4"

    from_square, to_square = parse_move("Ke2-e4Q")
    assert from_square == "e2" and to_square == "e4"
