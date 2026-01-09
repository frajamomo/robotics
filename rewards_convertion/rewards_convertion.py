import argparse
from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    """Abstract base class for conversion strategies (Strategy Pattern)."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the conversion type."""
        pass

    @property
    @abstractmethod
    def items(self) -> list:
        """Return the conversion table as list of (points, money) tuples."""
        pass

    @property
    def min_points(self) -> int:
        """Return the minimum points required for any redemption."""
        return min(points for points, _ in self.items)


class AmazonConversion(ConversionStrategy):
    """Amazon gift card conversion table."""

    @property
    def name(self) -> str:
        return "AMAZON"

    @property
    def items(self) -> list:
        return [
            (7, 5),
            (14, 10),
            (20, 15),
            (26, 20),
            (32, 25),
            (64, 50),
            (96, 75),
            (128, 100),
            (191, 150),
            (254, 200),
            (317, 250),
            (633, 500)
        ]


class MastercardConversion(ConversionStrategy):
    """Mastercard gift card conversion table."""

    @property
    def name(self) -> str:
        return "MASTERCARD"

    @property
    def items(self) -> list:
        return [
            (31, 25),
            (62, 50),
            (124, 100),
            (185, 150),
            (247, 200),
            (305, 250),
            (436, 350),
            (503, 400),
            (639, 500),
            (960, 750),
            (1280, 1000)
        ]


# Registry of available conversion strategies
CONVERSION_STRATEGIES = {
    'amazon': AmazonConversion,
    'mastercard': MastercardConversion,
}


def get_conversion_strategy(name: str) -> ConversionStrategy:
    """Factory function to get a conversion strategy by name."""
    name_lower = name.lower()
    if name_lower not in CONVERSION_STRATEGIES:
        available = ', '.join(CONVERSION_STRATEGIES.keys())
        raise ValueError(f"Unknown conversion type '{name}'. Available: {available}")
    return CONVERSION_STRATEGIES[name_lower]()


def maximize_money(max_points: int, strategy: ConversionStrategy):
    """
    Calculates the best combination of cards to maximize the money obtained
    from a given total number of points, using dynamic programming.
    """
    items = strategy.items

    # Initialize DP and Choice arrays
    dp = [-1] * (max_points + 1)
    dp[0] = 0
    choice = [-1] * (max_points + 1)

    # --- Dynamic Programming Calculation ---
    for current_p in range(1, max_points + 1):
        for item_index, (points, money) in enumerate(items):
            if current_p >= points:
                prev_dp = dp[current_p - points]
                if prev_dp != -1:
                    new_money = prev_dp + money
                    if new_money > dp[current_p]:
                        dp[current_p] = new_money
                        choice[current_p] = item_index

    # --- Find the Maximum Result ---
    max_money = -1
    max_points_index = -1

    for p in range(max_points + 1):
        if dp[p] > max_money:
            max_money = dp[p]
            max_points_index = p

    # --- Traceback to Reconstruct Combination ---
    combination = {}
    current_points = max_points_index

    while current_points > 0 and choice[current_points] != -1:
        item_index = choice[current_points]
        points_used, money_gained = items[item_index]
        combination[money_gained] = combination.get(money_gained, 0) + 1
        current_points -= points_used

    # --- Final Output Metrics & Formatting ---
    points_used_in_combination = max_points_index
    points_remaining = max_points - points_used_in_combination

    combination_details = []
    # Sort items by money value descending for cleaner output
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    # Prepare data rows and calculate max widths
    data_rows = []

    # Initialize maximum widths based on header length
    col_widths = {
        'Money ($M$)': len('Money ($M$)'),
        'Points per Card': len('Points per Card'),
        'Count': len('Count'),
        'Total Points': len('Total Points')
    }

    # Populate rows and update max widths
    for points_per_card, money_gained in sorted_items:
        count = combination.get(money_gained, 0)
        if count > 0:
            total_points = count * points_per_card
            row = {
                'Money ($M$)': f"${money_gained}",
                'Points per Card': str(points_per_card),
                'Count': str(count),
                'Total Points': str(total_points)
            }
            data_rows.append(row)

            # Update max widths
            for key in col_widths:
                col_widths[key] = max(col_widths[key], len(row[key]))

    return (max_money, points_used_in_combination, points_remaining, data_rows, col_widths)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate optimal gift card combination to maximize money from points."
    )
    parser.add_argument(
        '-t', '--type',
        choices=list(CONVERSION_STRATEGIES.keys()),
        default='amazon',
        help="Conversion type to use (default: amazon)"
    )
    parser.add_argument(
        'points',
        type=int,
        nargs='?',
        help="Total points available (if not provided, will prompt)"
    )
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()

    # Get the conversion strategy
    strategy = get_conversion_strategy(args.type)

    # Get points input
    if args.points is not None:
        points_input = args.points
    else:
        try:
            points_input = int(input("Enter the total number of points available: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            exit(1)

    min_required = strategy.min_points
    if points_input < min_required:
        print(f"Total points ({points_input}) is too low. You need at least {min_required} points to redeem a {strategy.name} card.")
        exit(1)

    # Run the calculation
    max_money, points_used, points_remaining, combination_rows, col_widths = maximize_money(points_input, strategy)

    # Output the results
    print("\n" + "="*60)
    print(f"| CALCULATING OPTIMAL {strategy.name} COMBINATION FOR {points_input} POINTS")
    print("="*60)

    if max_money == -1:
        print(f"ERROR: Could not find a valid combination for {points_input} points.")
    else:
        print(f"| Maximum Money Obtainable: ${max_money}")
        print(f"| Total Points Used:        {points_used}")
        print(f"| Points Remaining:         {points_remaining}")
        print("="*60)
        print("\nOptimal Combination of Cards:")

        # Define headers and their corresponding keys
        headers = ["Money ($M$)", "Points per Card", "Count", "Total Points"]

        # Function to format a row with fixed width
        def format_row(data_list, widths):
            formatted_parts = []
            # Right-justify all columns except the first one (Money)
            for i, (header, item) in enumerate(zip(headers, data_list)):
                width = widths[header]
                if i == 0:
                    formatted_parts.append(f"{item:<{width}}")  # Left-justify Money
                else:
                    formatted_parts.append(f"{item:>{width}}")  # Right-justify numbers
            return "| " + " | ".join(formatted_parts) + " |"

        # Print Header Row
        print(format_row(headers, col_widths))

        # Print Separator
        separator = ['-' * col_widths[h] for h in headers]
        print(format_row(separator, col_widths).replace(' ', '-'))

        # Print Data Rows
        for item in combination_rows:
            data_list = [
                item['Money ($M$)'],
                item['Points per Card'],
                item['Count'],
                item['Total Points']
            ]
            print(format_row(data_list, col_widths))

    print("\n" + "="*60)


if __name__ == "__main__":
    main()
