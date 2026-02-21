import math


def round_to_100(amount: float):
    """
    Round expense to next multiple of 100.
    Returns ceiling and remanent.
    """
    ceiling = math.ceil(amount / 100) * 100
    remanent = ceiling - amount
    return ceiling, remanent
