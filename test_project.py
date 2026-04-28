import csv
import os
from project import calculate_total_expenses

TEST_FILE = "test_expenses.csv"


def setup_module():
    """Create a test CSV file before tests run"""
    with open(TEST_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["2026-02-01", "Coffee", "Food", "30"])
        writer.writerow(["2026-02-02", "Taxi", "Transport", "120"])
        writer.writerow(["2026-02-03", "Snacks", "Food", "50"])


def teardown_module():
    """Remove test CSV file after tests run"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_calculate_total_expenses():
    assert calculate_total_expenses(TEST_FILE) == 200


def test_empty_file():
    empty_file = "empty.csv"
    open(empty_file, "w").close()
    assert calculate_total_expenses(empty_file) == 0
    os.remove(empty_file)


def test_file_not_found():
    assert calculate_total_expenses("does_not_exist.csv") == 0
