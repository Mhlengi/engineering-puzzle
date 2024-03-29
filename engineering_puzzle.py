from functions import find_subset_given_exactly_value_sum

list_of_areas_data_set = [
    18897109,
    12828837,
    9661105,
    6371773,
    5965343,
    5926800,
    5582170,
    5564635,
    5268860,
    4552402,
    4335391,
    4296250,
    4224851,
    4192887,
    3439809,
    3279933,
    3095213,
    2812896,
    2783243,
    2710489,
    2543482,
    2356285,
    2226009,
    2149127,
    2142508,
    2134411
]
exactly_value_sum = 101000000

subset_areas = find_subset_given_exactly_value_sum(
    list_of_areas_data_set,
    exactly_value_sum
)

print(subset_areas)
