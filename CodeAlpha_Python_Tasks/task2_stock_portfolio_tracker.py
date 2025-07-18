
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2700, "MSFT": 300}
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in our price list.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

total_investment = sum(stock_prices[s] * q for s, q in portfolio.items())
print("\nYour portfolio summary:")
for s, q in portfolio.items():
    print(f"{s}: {q} shares @ {stock_prices[s]} each")

print(f"\nTotal Investment Value: ${total_investment}")
