import io
import sys
import pytest
from solution import plusMinus

def run_plus_minus(input_data):
    # Redirect stdin
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    plusMinus(arr)

    # Get output
    return sys.stdout.getvalue().strip()

def test_case_1():
    input_data = "6\n-4 3 -9 0 4 1\n"
    expected_output = "0.500000\n0.333333\n0.166667"
    assert run_plus_minus(input_data) == expected_output

def test_case_2():
    input_data = "3\n1 1 1\n"
    expected_output = "1.000000\n0.000000\n0.000000"
    assert run_plus_minus(input_data) == expected_output

def test_case_3():
    input_data = "3\n-1 -1 -1\n"
    expected_output = "0.000000\n1.000000\n0.000000"
    assert run_plus_minus(input_data) == expected_output

def test_case_4():
    input_data = "4\n0 0 0 0\n"
    expected_output = "0.000000\n0.000000\n1.000000"
    assert run_plus_minus(input_data) == expected_output
