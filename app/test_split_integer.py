from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(6, 3)) == 6
    assert sum(split_integer(8, 4)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(8, 1)) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 3)

    assert len(result) == 3
    assert sum(result) == 6
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(6, 1) == [6]
    assert split_integer(10, 1) == [10]
    assert split_integer(50, 1) == [50]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 3)

    assert len(result) == 3
    assert sum(result) == 1
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_distribution_should_be_balanced() -> None:
    result = split_integer(10, 3)

    assert len(result) == 3
    assert sum(result) == 10
    assert max(result) - min(result) <= 1