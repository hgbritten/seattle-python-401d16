from fizz_buzz.fizzy import fizz_buzz


def test_one():
    actual = fizz_buzz(1)
    expected = "1"
    assert actual == expected


def test_two():
    actual = fizz_buzz(2)
    expected = "2"
    assert actual == expected


def test_three():
    actual = fizz_buzz(3)
    expected = "Fizz"
    assert actual == expected


def test_six():
    actual = fizz_buzz(6)
    expected = "Fizz"
    assert actual == expected


def test_five():
    actual = fizz_buzz(5)
    expected = "Buzz"
    assert actual == expected


def test_fifteen():
    actual = fizz_buzz(15)
    expected = "FizzBuzz"
    assert actual == expected
