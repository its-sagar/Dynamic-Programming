'''
Description
Given an array of positive integers nums and an integer target, determine
if there exists any subset of numbers from the array whose elements add up exactly to
the target. Each number in the array can be used at most once.

Objective
Write a function can_reach_target(nums: list[int], target: int) -> bool that returns True
if a valid subset sum equals the target, and False otherwise.

'''


def can_reach_target(nums: list[int], target: int) -> bool:
    n=len(nums)
    dp = [[True if j == 0 else False for j in range(target+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, target+1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]





def run_target_sum_tests(test_function):
    """
    Test runner that accepts a target sum function as an argument 
    and validates it against multiple scenario test cases.
    """
    # Define test cases: (nums, target, expected_output, description)
    test_cases = [
        ([1, 2, 6, 3], 4, True, "Standard Case (1 + 3 = 4)"),
        ([1, 2, 6, 3], 6, True, "Exact Element Match"),
        ([1, 2, 6, 3], 8, True, "Possible Combination (2 + 6 = 8)"),
        ([1, 2, 3], 0, True, "Zero Target Edge Case"),
        ([1, 2, 3], 10, False, "Target Larger Than Total Sum"),
        ([5], 5, True, "Single Element Match"),
        ([5], 2, False, "Single Element Mismatch")
    ]
    
    passed_count = 0
    print(f"--- Running tests for function: '{test_function.__name__}' ---\n")
    
    for i, (nums, target, expected, desc) in enumerate(test_cases, 1):
        try:
            # Execute the function passed as an argument
            result = test_function(nums, target)
            
            if result == expected:
                print(f"✅ Test {i} PASSED: {desc}")
                passed_count += 1
            else:
                print(f"❌ Test {i} FAILED: {desc}")
                print(f"   Input: nums={nums}, target={target}")
                print(f"   Expected: {expected}, Got: {result}")
        except Exception as e:
            print(f"💥 Test {i} ERROR: {desc}")
            print(f"   Exception raised: {e}")
            
    print(f"\n--- Results: {passed_count}/{len(test_cases)} tests passed ---")


run_target_sum_tests(can_reach_target)




