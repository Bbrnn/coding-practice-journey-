# Plus Minus – HackerRank Challenge

## Problem
Given an array of integers, calculate the fractions of its elements that are:
- positive
- negative
- zero

Each fraction should be printed on a new line with **6 decimal places**.

### Example
Input:

-4 3 -9 0 4 1

Output:

0.500000
0.333333
0.166667

Explanation:

- There are 3 positive numbers: `3, 4, 1`
- There are 2 negative numbers: `-4, -9`
- There is 1 zero: `0`

Fractions:
- Positive → `3/6 = 0.500000`
- Negative → `2/6 = 0.333333`
- Zero → `1/6 = 0.166667`

---

## Approach
1. Count the number of positive, negative, and zero elements.
2. Divide each count by the total number of elements (`n`).
3. Print the results, formatted to **6 decimal places**.
