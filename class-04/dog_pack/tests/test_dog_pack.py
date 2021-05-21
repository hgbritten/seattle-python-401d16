import pytest
from dog_pack.dogs import Boxer, Puggle, matrix, fibonacci


def test_fibonacci():
    actual = fibonacci(2)
    expect = 1
    assert actual == expect


def test_matrix():
    actual = matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
    expected = [6, 12, 21]
    assert actual == expected


def test_boxer_import():
    assert Boxer


def test_boxer_create():
    assert Boxer()  # no "new" needed


def test_boxer_with_name(marv):

    actual = marv.name
    expected = "Marv"
    actual == expected


def test_boxer_with_no_name():
    pooch = Boxer()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


def test_boxer_greet(marv):

    actual = marv.greet()
    excepted = "The name's Marv. Pleasure"
    assert actual == excepted


def test_boxer_greet(lela):

    actual = lela.greet()
    excepted = "I am Lela. I am SO HAPPY to meet you!"
    assert actual == excepted


def test_boxer_sleep(marv):

    actual = marv.sleep()
    expected = "zzz"
    assert actual == expected


@pytest.fixture
def marv():
    return Boxer("Marv")


@pytest.fixture
def lela():
    return Puggle("Lela")
