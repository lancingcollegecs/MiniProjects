import mastermind as m


def test_scores_blackPegs():
    assert m.score("royg", "royg") == "bbbb"
    assert m.score("royg", "royb") == "bbb"
def test_scores_whitePegs():
    assert m.score("royg", "bbgy") == "ww"
    assert m.score("royg", "oygr") == "wwww"
def test_scores_mixedPegs():
    assert m.score("roro", "rrgr") == "bw"
    assert m.score("royg", "rrgr") == "bw"
    assert m.score("rrrg", "ygro") == "bw"
def test_scores_erronious():
    assert m.score("rrrr", "rrrrr") == "bbbb"
    assert m.score("royy", "roy") == "bbb"
    assert m.score("royg", "") == ""
