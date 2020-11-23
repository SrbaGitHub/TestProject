import pytest


@pytest.mark.math
def test_multiply_two_positive_ints():
  assert 2 * 3 == 6


@pytest.mark.math
def test_multiply_identity():
  assert 1 * 99 == 99


@pytest.mark.math
def test_multiply_zero():
  assert 0 * 100 == 0
