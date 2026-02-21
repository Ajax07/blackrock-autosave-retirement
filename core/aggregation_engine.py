def aggregate_by_k(transactions, k_periods):
    output = []

    for k in k_periods:
        total = sum(
            tx["remanent"]
            for tx in transactions
            if k.start <= tx["timestamp"] <= k.end
        )

        output.append({
            "start": k.start,
            "end": k.end,
            "amount": total
        })

    return output
