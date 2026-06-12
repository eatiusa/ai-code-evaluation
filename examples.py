def two_sum_hashmap(nums, target):
    """
    Preferred solution.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    seen = {}

    for index, number in enumerate(nums):
        difference = target - number

        if difference in seen:
            return [seen[difference], index]

        seen[number] = index

    return []


def two_sum_bruteforce(nums, target):
    """
    Less preferred solution.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print("Hash Map Solution:", two_sum_hashmap(nums, target))
    print("Brute Force Solution:", two_sum_bruteforce(nums, target))
