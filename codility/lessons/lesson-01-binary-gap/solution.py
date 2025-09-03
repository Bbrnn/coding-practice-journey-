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
