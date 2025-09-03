# Test Cases for Binary Gap

We test the `binary_gap` function with different inputs to make sure it works correctly.

---

## Basic Cases
| Input (N) | Binary Representation | Expected Output | Explanation |
|-----------|------------------------|-----------------|-------------|
| 9         | 1001                   | 2               | Two zeros between ones |
| 529       | 1000010001              | 4               | Longest gap is 4 |
| 20        | 10100                  | 1               | Only one zero between ones |
| 15        | 1111                   | 0               | No zeros between ones |

---

## Edge Cases
| Input (N) | Binary Representation | Expected Output | Explanation |
|-----------|------------------------|-----------------|-------------|
| 1         | 1                      | 0               | No zeros at all |
| 2         | 10                     | 0               | No zeros between ones |
| 32        | 100000                 | 0               | Trailing zeros don’t count |
| 1041      | 10000010001            | 5               | Longest gap is 5 |

---

## Python Test Code
```python
def test_binary_gap():
    assert binary_gap(9) == 2
    assert binary_gap(529) == 4
    assert binary_gap(20) == 1
    assert binary_gap(15) == 0
    assert binary_gap(1) == 0
    assert binary_gap(2) == 0
    assert binary_gap(32) == 0
    assert binary_gap(1041) == 5
    print("All tests passed!")

test_binary_gap()
