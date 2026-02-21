def nps_tax_deduction(invested, annual_income):
    return min(invested, 0.10 * annual_income, 200000)
