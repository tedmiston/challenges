def answer(meetings):
    """
    Given a list of meeting requests (meetings input param), return the
    maximum number of non-overlapping meetings that can be scheduled (i.e.,
    the interval scheduling problem).

    meetings - A list of lists where each element is a two-element list
    denoting a meeting request by its start time and end time.

    Assumes the length of time in a day is 1,000,000 of whatever arbitrary
    unit of time is implied by this problem.
    """
    sorted_meetings = sorted(meetings, key=lambda i: i[1])

    scheduled_jobs = 0
    last_finish = 0
    while sorted_meetings:
        start, finish = sorted_meetings.pop(0)
        if start >= last_finish:
            scheduled_jobs += 1
            last_finish = finish

    return scheduled_jobs

assert answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]) == 4
assert answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]]) == 1
