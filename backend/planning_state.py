def optimize_schedule(tasks, deps=None):
    """
    Basic linear scheduler if CPM not used.
    """

    if not tasks:
        return {}

    schedule = {}

    day = 1
    for t in tasks:
        schedule[t] = 3  # default duration
        day += 3

    return schedule
