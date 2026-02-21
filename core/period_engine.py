def in_range(ts, start, end):
    return start <= ts <= end


def apply_period_rules(transactions, q_periods, p_periods):
    """
    Apply q and p rules.
    """

    for tx in transactions:

        # q override
        applicable_q = [
            q for q in q_periods
            if in_range(tx["timestamp"], q.start, q.end)
        ]

        if applicable_q:
            latest = max(applicable_q, key=lambda x: x.start)
            tx["remanent"] = latest.fixed

        # p addition
        for p in p_periods:
            if in_range(tx["timestamp"], p.start, p.end):
                tx["remanent"] += p.extra

    return transactions
