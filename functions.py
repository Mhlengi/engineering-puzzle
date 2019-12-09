from itertools import combinations


def find_subset_given_exactly_value_sum(data_list, value_sum):
    subset_list = []
    for value in range(len(data_list)):
        subset_list.extend(
            [
                combination for combination in combinations(data_list, value)
                if sum(combination) == value_sum
            ]
        )

    return subset_list[0] if len(subset_list) > 0 else ()
