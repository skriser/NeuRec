def hit(rank_list, target_items):
    count = 0
    for item in rank_list:
        if item in target_items:
            count += 1
    return count


def getRec(rank_list, target_items):
    return hit(rank_list, target_items) / len(target_items)
