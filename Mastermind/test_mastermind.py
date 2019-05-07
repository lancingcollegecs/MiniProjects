import mastermind as m
import pytest


def test_scores():
    assert m.score("royg", "royg") == "bbbb"
    assert m.score("roro", "rrgr") == "bw"
    assert m.score("royg", "rogy") == "bbww"
    assert m.score("royg", "oryg") == "bbww"
    assert m.score("oygr", "royg") == "wwww"
    assert m.score("royg", "rrgr") == "bw"
    assert m.score("rrrg", "yogr") == "ww"
