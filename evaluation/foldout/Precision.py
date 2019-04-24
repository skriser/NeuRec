def hit(rank_list, target_items):
    count = 0
    for item in rank_list:
        if item in target_items:
            count += 1
    return count


def getPre(rank_list, target_items, topK):
    return hit(rank_list, target_items) / topK
