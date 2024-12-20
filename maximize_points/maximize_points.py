def maximize_euros(points_to_euros, max_points):
    """
    Finds the combination of euros and points that maximizes the euros for the given points limit.

    Parameters:
        points_to_euros (list of tuples): A list of (euros, points) pairs.
        max_points (int): The maximum number of points available.

    Returns:
        tuple: The maximum euros and the combination of (euros, points) used to achieve it.
    """
    n = len(points_to_euros)
    dp = [0] * (max_points + 1)
    combinations = [[] for _ in range(max_points + 1)]

    # Fill the DP table
    for euros, points in points_to_euros:
        for p in range(max_points, points - 1, -1):
            if dp[p - points] + euros > dp[p]:
                dp[p] = dp[p - points] + euros
                combinations[p] = combinations[p - points] + [(euros, points)]

    # Result: maximum euros and the combination
    max_euros = dp[max_points]
    best_combination = combinations[max_points]

    return max_euros, best_combination

# Data from the table
points_to_euros = [
    (25, 28),
    (50, 55),
    (100, 110),
    (150, 165),
    (200, 220),
    (250, 272),
    (350, 389),
    (400, 449),
    (500, 570),
    (750, 857),
    (1000, 1142)
]

# Example usage
max_points = 536
max_euros, best_combination = maximize_euros(points_to_euros, max_points)

print(f"Maximum euros: {max_euros}")
print("Best combination:")
for euros, points in best_combination:
    print(f"- {euros} euros ({points} points)")

