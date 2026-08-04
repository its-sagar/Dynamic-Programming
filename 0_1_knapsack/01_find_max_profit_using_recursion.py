'''
0/1 Knapsack Problem Using Recursion
Given the weights and profits of n items, put these items in a
knapsack of capacity(capacity) to get the maximum total profit in the knapsack.
You cannot break an item; you must either pick it entirely or leave it (0/1 property).
'''


def findMaxProfit(weights: list[int], profits: list[int], capacity: int, n: int):
    if capacity == 0 or n == 0:
        return 0
    
    if (weights[n-1] <= capacity):
        return max((profits[n-1] + findMaxProfit(weights, profits, capacity-weights[n-1], n-1)),
                   findMaxProfit(weights, profits, capacity, n-1))
    else:
        return findMaxProfit(weights, profits, capacity, n-1)



def run_tests(findMaxProfit):
    """Automates validation of the knapsack implementation."""
    test_cases = [
        {
            "name": "Standard Case",
            "weights": [10, 20, 30], "profits": [60, 100, 120], "capacity": 50, "n": 3,
            "expected": 220
        },
        {
            "name": "Zero Capacity",
            "weights": [10, 20, 30], "profits": [60, 100, 120], "capacity": 0, "n": 3,
            "expected": 0
        },
        {
            "name": "Empty Arrays",
            "weights": [], "profits": [], "capacity": 50, "n": 0,
            "expected": 0
        },
        {
            "name": "No Items Fit",
            "weights": [50, 60, 70], "profits": [10, 20, 30], "capacity": 30, "n": 3,
            "expected": 0
        },
        {
            "name": "All Items Fit",
            "weights": [5, 10, 15], "profits": [10, 20, 30], "capacity": 40, "n": 3,
            "expected": 60
        },
        {
            "name": "Duplicate Weights",
            "weights": [10, 10, 10], "profits": [50, 100, 150], "capacity": 20, "n": 3,
            "expected": 250
        },
        {
            "name": "Greedy Choice Failure",
            "weights": [20, 10, 10], "profits": [100, 55, 55], "capacity": 20, "n": 3,
            "expected": 110
        }
    ]

    print(f"--- Running Tests for {findMaxProfit.__name__} ---")
    passed = 0
    for tc in test_cases:
        result = findMaxProfit(tc["weights"], tc["profits"], tc["capacity"], tc["n"])
        try:
            assert result == tc["expected"], f"Expected {tc['expected']}, but got {result}"
            print(f"✅ {tc['name']}: Passed")
            passed += 1
        except AssertionError as e:
            print(f"❌ {tc['name']}: Failed ({e})")
            
    print(f"Result Matrix Format: Passed {passed}/{len(test_cases)} tests.\n")

# Run tests on both implementations
if __name__ == "__main__":
    run_tests(findMaxProfit)
