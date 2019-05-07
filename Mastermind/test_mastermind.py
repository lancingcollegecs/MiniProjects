import mastermind as m
import pytest


def test_scores():
    assert m.score(list("royg"), list("royg")) == list("bbbb")
    assert m.score(list("roro"), list("rrgr")) == list("bw")
    assert m.score(list("royg"), list("rogy")) == list("bbww")
    assert m.score(list("royg"), list("oryg")) == list("bbww")
    assert m.score(list("oygr"), list("royg")) == list("wwww")
    assert m.score(list("royg"), list("rrgr")) == list("bw")
    assert m.score(list("rrrg"), list("yogr")) == list("ww")
