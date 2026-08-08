'''
Given an array of positive integers nums and an integer target_sum, determine if
the array can be partitioned into exactly two subsets such that:The sum of
elements in the first subset equals the sum of elements in the second subset.
The sum of each subset is exactly equal to the provided target_sum.

In other words, a valid partition exists only if the total sum of all elements 
in the array is equal to 2 * target_sum. If the total sum does not
equal 2 * target_sum, or if the array cannot be split into two equal halves
that match this target, return False
'''

def subsetTargetSum(nums: list[int], target: int, n: int) -> bool:
    dp = [ [ True if j == 0 else False for j in range(target+1) ] for i in range(n+1) ]

    for i in range(n+1):
        for j in range(target+1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]

def equalSumPartition(nums: list[int], target: int) -> bool:
    n = len(nums)
    if n == 0 and target == 0:
        return True
    if n == 0 and target > 0:
        return False
    
    totalSum = 0
    for i in range(n):
        totalSum += nums[i]

    if totalSum % 2 != 0:
        return False
    else:
        return subsetTargetSum(nums, target, n)



def run_tests(implementation_function):
    """Runs test cases verifying the two-subset equal partition rule."""
    test_cases = [
        # (nums, target_sum, expected_output, description)
        ([1, 5, 11, 5], 11, True, "Valid split: [1, 5, 5] and [11]"),
        ([1, 2, 3, 5], 5, False, "Fail: Total sum (11) is not 2 * target_sum (10)"),
        ([1, 2, 5], 4, False, "Fail: Total sum matches 8, but cannot form subset of 4"),
        ([3, 3], 3, True, "Valid split: Two identical single-element subsets"),
        ([10, 20, 30], 30, True, "Valid split: [10, 20] and [30]"),
        ([1, 1, 1, 1], 2, True, "Valid split: [1, 1] and [1, 1]"),
        ([2, 4, 6], 5, False, "Fail: Target 5 is impossible with even total sum 12"),
        ([], 0, True, "Edge case: Empty array splits into two empty subsets summing to 0"),
    ]
    
    passed = 0
    for i, (nums, target, expected, desc) in enumerate(test_cases, 1):
        result = implementation_function(nums, target)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
            passed += 1
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: nums={nums}, target_sum={target}")
            print(f"   Expected: {expected}, Got: {result}")
            
    print(f"\nScore: {passed}/{len(test_cases)} tests passed.")


run_tests(equalSumPartition)