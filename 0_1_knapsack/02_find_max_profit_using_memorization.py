'''
0/1 Knapsack Problem Using Memorization
Given the weights and profits of n items, put these items in a
knapsack of capacity(capacity) to get the maximum total profit in the knapsack.
You cannot break an item; you must either pick it entirely or leave it (0/1 property).
'''


def find_max_profit(weights: list[int], profits: list[int], capacity: int, n: int):
    if capacity == 0 or n == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n-1] <= capacity:
        memo[n][capacity] = max(profits[n-1] + find_max_profit(weights, profits, capacity-weights[n-1], n-1),
                                find_max_profit(weights, profits, capacity, n-1))

    else:
        memo[n][capacity] = find_max_profit(weights, profits, capacity, n-1)

    return memo[n][capacity]

def checkTestCase(result, expectedOutput):
    if result == expectedOutput:
        print("Test Case Passed!")
    else:
        print("Test Case Failed!")



weights =   [1, 2, 3, 2, 4, 1]
profits = [2, 3, 4, 6, 2, 1]
capacity = 10
n = len(weights)
expectedOutput = 16
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50
n = len(weights)
expectedOutput = 220
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 0
n = 3
expectedOutput = 0
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = []
profits = []
capacity = 50
n = len(weights)
expectedOutput = 0
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = [50, 60, 70]
profits = [10, 20, 30]
capacity = 30
n = len(weights)
expectedOutput = 0
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = [5, 10, 15]
profits = [10, 20, 30]
capacity = 40
n = len(weights)
expectedOutput = 60
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = [10, 10, 10]
profits = [50, 100, 150]
capacity = 20
n = len(weights)
expectedOutput = 250
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)

weights = [20, 10, 10]
profits = [100, 55, 55]
capacity = 20
n = len(weights)
expectedOutput = 110
rows = len(weights) + 1
cols = capacity + 1
memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
result = find_max_profit(weights, profits, capacity, n)
checkTestCase(result, expectedOutput)