# Define stock symbols and corresponding company names
stocks = {
    'AAPL': 'Apple',
    'GOOGL': 'Alphabet',
    'MSFT': 'Microsoft',
    'AMZN': 'Amazon',
    'TSLA': 'Tesla'
}

# Define historical stock prices (daily closing prices for simplicity)
stock_prices = {
    'AAPL': [150, 160, 155, 170, 180],  # Replace with actual historical data
    'GOOGL': [1200, 1250, 1180, 1300, 1350],
    'MSFT': [80, 85, 82, 90, 92],
    'AMZN': [1800, 1900, 1850, 2000, 2100],
    'TSLA': [300, 320, 310, 340, 350]
}

# Function to calculate average annual return and risk
def calculate_annual_return_and_risk(prices):
    # Assuming prices are given in chronological order
    daily_returns = [(prices[i + 1] - prices[i]) / float(prices[i]) for i in range(len(prices) - 1)]
    annual_return = ((float(prices[-1]) / prices[0]) ** (1.0 / len(prices))) - 1.0
    daily_return_squared = [(r - annual_return) ** 2 for r in daily_returns]
    risk = (sum(daily_return_squared) / float(len(daily_return_squared))) ** 0.5 * (252.0 ** 0.5)  # Assuming 252 trading days in a year

    return annual_return, risk

# Calculate and display the average annual return and risk for each company
print "Company\t\tSymbol\t\tAverage Annual Return\tRisk"
print "="*60
for symbol, name in stocks.items():
    annual_return, risk = calculate_annual_return_and_risk(stock_prices[symbol])
    print "{0}\t\t{1}\t\t{2:.2%}\t\t\t{3:.2%}".format(name, symbol, annual_return, risk)

# Calculate and display the overall portfolio return and risk
portfolio_returns = [calculate_annual_return_and_risk(stock_prices[symbol])[0] for symbol in stocks]
portfolio_risks = [calculate_annual_return_and_risk(stock_prices[symbol])[1] for symbol in stocks]

portfolio_return = sum(portfolio_returns) / float(len(stocks))
portfolio_risk = (sum(portfolio_risks) / float(len(portfolio_risks))) ** 0.5

print "\nOverall Portfolio Performance:"
print "Portfolio Return: {0:.2%}".format(portfolio_return)
print "Portfolio Risk: {0:.2%}".format(portfolio_risk)
