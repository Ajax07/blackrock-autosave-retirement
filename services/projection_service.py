def future_value(P, r, years):
    return P * ((1 + r) ** years)


def inflation_adjusted(value, inflation, years):
    return value / ((1 + inflation) ** years)


def investment_projection(P, rate, age, inflation):
    years = max(60 - age, 5)

    fv = future_value(P, rate, years)
    real = inflation_adjusted(fv, inflation, years)

    return {
        "future_value": fv,
        "real_value": real,
        "years": years
    }
