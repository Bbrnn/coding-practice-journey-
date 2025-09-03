# Codility Lesson 1 – Binary Gap

## Problem Statement
A binary gap is the longest sequence of consecutive zeros surrounded by ones in the binary representation of a positive integer.

- Example:  
  - N = 529 → Binary = `1000010001` → Longest gap = `4`  
  - N = 20  → Binary = `10100` → Longest gap = `1`  
  - N = 15  → Binary = `1111` → Longest gap = `0` (no gaps)  

## My Thought Process
1. Convert the number to binary (ignore the `0b` prefix).
2. Traverse the binary string:
   - Start counting zeros only after the first `1`.
   - When another `1` is found, close the gap and compare with the maximum gap found so far.
   - Reset the counter to start counting a new gap.
   - Ignore leading and trailing zeros (handled naturally by starting only after the first `1`).
3. Return the largest gap length.

This is essentially a **state tracking problem**:
- `-1` → haven’t seen the first `1` yet.
- `0` → ready to count zeros after a `1`.
- `>0` → currently counting zeros.

## Solution Code
```python
def binary_gap(n):
    b = bin(n)[2:]          # binary string without '0b'
    max_gap = 0
    current_gap = -1        # -1 means we haven’t seen the first '1' yet
    
    for bit in b:
        if bit == '1':
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0  # start counting again
        elif bit == '0' and current_gap != -1:
            current_gap += 1
    
    return max_gap
