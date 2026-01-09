import pytest
from rewards_convertion import (
    AmazonConversion,
    MastercardConversion,
    get_conversion_strategy,
    maximize_money,
)


class TestConversionStrategies:
    """Tests for conversion strategy classes."""

    def test_amazon_strategy_name(self):
        strategy = AmazonConversion()
        assert strategy.name == "AMAZON"

    def test_mastercard_strategy_name(self):
        strategy = MastercardConversion()
        assert strategy.name == "MASTERCARD"

    def test_amazon_min_points(self):
        strategy = AmazonConversion()
        assert strategy.min_points == 7

    def test_mastercard_min_points(self):
        strategy = MastercardConversion()
        assert strategy.min_points == 31

    def test_get_conversion_strategy_amazon(self):
        strategy = get_conversion_strategy("amazon")
        assert isinstance(strategy, AmazonConversion)

    def test_get_conversion_strategy_mastercard(self):
        strategy = get_conversion_strategy("mastercard")
        assert isinstance(strategy, MastercardConversion)

    def test_get_conversion_strategy_case_insensitive(self):
        strategy = get_conversion_strategy("AMAZON")
        assert isinstance(strategy, AmazonConversion)

    def test_get_conversion_strategy_invalid(self):
        with pytest.raises(ValueError, match="Unknown conversion type"):
            get_conversion_strategy("invalid")


class TestMaximizeMoney:
    """Tests for the maximize_money function."""

    def test_zero_points_amazon(self):
        """Test with 0 points - should return -1 (no valid combination)."""
        strategy = AmazonConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(0, strategy)
        assert max_money == 0
        assert points_used == 0
        assert points_remaining == 0
        assert rows == []

    def test_zero_points_mastercard(self):
        """Test with 0 points for Mastercard."""
        strategy = MastercardConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(0, strategy)
        assert max_money == 0
        assert points_used == 0
        assert points_remaining == 0
        assert rows == []

    def test_insufficient_points_amazon(self):
        """Test with points below minimum (6 < 7 for Amazon).

        Returns 0 money since no cards can be redeemed but it's a valid state.
        """
        strategy = AmazonConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(6, strategy)
        assert max_money == 0
        assert points_used == 0
        assert points_remaining == 6
        assert rows == []

    def test_insufficient_points_mastercard(self):
        """Test with points below minimum (30 < 31 for Mastercard).

        Returns 0 money since no cards can be redeemed but it's a valid state.
        """
        strategy = MastercardConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(30, strategy)
        assert max_money == 0
        assert points_used == 0
        assert points_remaining == 30
        assert rows == []

    def test_exact_minimum_points_amazon(self):
        """Test with exactly 7 points for Amazon (minimum)."""
        strategy = AmazonConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(7, strategy)
        assert max_money == 5
        assert points_used == 7
        assert points_remaining == 0

    def test_exact_minimum_points_mastercard(self):
        """Test with exactly 31 points for Mastercard (minimum)."""
        strategy = MastercardConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(31, strategy)
        assert max_money == 25
        assert points_used == 31
        assert points_remaining == 0

    def test_amazon_100_points(self):
        """Test Amazon conversion with 100 points."""
        strategy = AmazonConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(100, strategy)
        assert max_money == 75
        assert points_used == 96
        assert points_remaining == 4

    def test_mastercard_500_points(self):
        """Test Mastercard conversion with 500 points."""
        strategy = MastercardConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(500, strategy)
        assert max_money == 400
        assert points_used == 490
        assert points_remaining == 10

    def test_combination_rows_structure(self):
        """Test that combination rows have correct structure."""
        strategy = AmazonConversion()
        _, _, _, rows, col_widths = maximize_money(100, strategy)

        assert len(rows) > 0
        for row in rows:
            assert 'Money ($M$)' in row
            assert 'Points per Card' in row
            assert 'Count' in row
            assert 'Total Points' in row

        assert 'Money ($M$)' in col_widths
        assert 'Points per Card' in col_widths
        assert 'Count' in col_widths
        assert 'Total Points' in col_widths

    def test_large_points_amazon(self):
        """Test with a large number of points for Amazon."""
        strategy = AmazonConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(1000, strategy)
        assert max_money > 0
        assert points_used <= 1000
        assert points_remaining >= 0
        assert points_used + points_remaining == 1000

    def test_large_points_mastercard(self):
        """Test with a large number of points for Mastercard."""
        strategy = MastercardConversion()
        max_money, points_used, points_remaining, rows, _ = maximize_money(2000, strategy)
        assert max_money > 0
        assert points_used <= 2000
        assert points_remaining >= 0
        assert points_used + points_remaining == 2000
