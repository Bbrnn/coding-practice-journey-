def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    arr_length = len(arr)

    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1

    # Print with 6 decimal places
    print(f"{pos_count / arr_length:.6f}")
    print(f"{neg_count / arr_length:.6f}")
    print(f"{zero_count / arr_length:.6f}")


if __name__ == '__main__':
    n = int(input().strip())  # size of array
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
