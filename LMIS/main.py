def longest_increasing_subsequence(arr):
    lis = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    index = lis.index(max_length)
    lmis = [arr[index]]

    for i in range(index - 1, -1, -1):
        if arr[i] < arr[index] and lis[i] == lis[index] - 1:
            lmis.insert(0, arr[i])
            index = i

    return max_length, lmis


if __name__ == "__main__":
    arr = [3, 10, 2, 1, 20, 5, 15, 6, 7, 8, 14, 21, 18, 11, 25, 12, 9, 24, 30]
     
    length, lmis_sequence = longest_increasing_subsequence(arr)

    print(f"Given Input: {arr}")
    print(f"Length of Longest Monotonically Increasing Subsequence: {length}")
    print("Longest Monotonically Increasing Subsequence:", lmis_sequence)
