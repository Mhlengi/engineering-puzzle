import unittest

from functions import find_subset_given_exactly_value_sum


class TestFindSubsetGivenExactlyValueSum(unittest.TestCase):
    def test_find_subset_given_exactly_value_sum_with_valid_data_1_input(self):
        local_list = [3, 5, 7, 10]
        total_exactly = 15
        subset = find_subset_given_exactly_value_sum(local_list, total_exactly)

        expected_subset = (5, 10)

        self.assertEqual(subset, expected_subset)

    def test_find_subset_given_exactly_value_sum_with_valid_data_2_input(self):
        local_list = [10, 7, 5, 3]
        total_exactly = 15
        subset = find_subset_given_exactly_value_sum(local_list, total_exactly)

        expected_subset = (10, 5)

        self.assertEqual(subset, expected_subset)

    def test_find_subset_given_exactly_value_sum_with_invalid_data_input(self):
        local_list = [10, 7, 5, 3]
        total_exactly = 18
        subset = find_subset_given_exactly_value_sum(local_list, total_exactly)

        expected_subset = (10, 5)

        self.assertNotEqual(subset, expected_subset)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
