from logic_utils import check_guess, parse_guess, get_range_for_difficulty


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_blank():
    ok, guess, err = parse_guess("")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_non_number():
    ok, guess, err = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."


def test_parse_guess_decimal_rejected():
    ok, guess, err = parse_guess("12.5")
    assert ok is False
    assert guess is None
    assert err == "Please enter a whole number."


def test_get_range_for_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_get_range_for_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)