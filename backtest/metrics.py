def sharpe_ratio(returns, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / returns.std() * (252 ** 0.5)

def max_drawdown(equity_curve):
    drawdowns = (equity_curve / equity_curve.cummax() - 1)
    return drawdowns.min()

def cagr(initial_value, final_value, periods):
    return (final_value / initial_value) ** (1 / periods) - 1

def volatility(returns):
    return returns.std() * (252 ** 0.5)