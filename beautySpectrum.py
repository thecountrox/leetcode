def get_subarray_beauty(nums, k, x):
    """
    Write your logic here.
    Parameters:
        nums (list): List of integers representing the amount of money each customer spent.
        k (int): Size of the subarrays to consider.
        x (int): Some value X as per problem statement.
    Returns:
        list: List of integers representing the beauty of the subarrays.
    """
    l = 0
    r = k + 1

    res = []

    while r <= len(nums):

        g = sorted(nums[l:r])[x - 1]
        if g < 0:
            res.append(g)
        else:
            res.append(0)

        l += 1
        r += 1

    return res


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    k = int(data[0])  # First input is the integer k
    x = int(data[1])  # Second input is the integer x
    n = int(data[2])  # Third input is the integer n
    nums = list(map(int, data[3:]))  # Remaining input is the array of integers

    # Call user logic function and get the result
    result = get_subarray_beauty(nums, k, x)

    # Print the output as space-separated integers
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
