#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    total_sum = 0
    total_weight = 0

    for score in my_list:
        total_sum += (score[0] * score[1])
        total_weight += score[1]
    return (total_sum / total_weight)
