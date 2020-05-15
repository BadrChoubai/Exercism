def latest(scores: list) -> int:
    return scores[-1]


def personal_best(scores: list) -> int:
    return max(scores)


def personal_top_three(scores: list) -> [int]:
    return sorted(scores, reverse=True)[:3]
