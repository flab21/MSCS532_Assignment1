def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Standard insertion sort shifts while arr[i] > key (ascending).
        # Flipping to < gives monotonically decreasing order instead.
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    test_cases = [
        [5, 2, 9, 1, 5, 6],   # general case
        [3, 3, 3, 3],         # all duplicate values
        [7],                  # single element
        [],                   # empty list
    ]

    for case in test_cases:
        original = case.copy()
        insertion_sort(case)
        print(f"Before: {original}")
        print(f"After:  {case}")
        print()