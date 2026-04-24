import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
amounts = [7, 50, 10, 20, 25]

amounts_series = pd.Series(amounts, index=tickers)

data = yf.download(tickers, period="5d", group_by='ticker')

latest_prices = pd.Series({
    ticker: data[ticker]['Close'].dropna().iloc[-1]
    for ticker in tickers
})


total = latest_prices * amounts_series


portfolio_df = sorted(pd.DataFrame({
    'Price': latest_prices,
    'Shares': amounts_series,
    'Value': total
}))

print(portfolio_df)
print("\nTotal Portfolio Value:", portfolio_df['Value'].sum())

# Visualization
fig, ax = plt.subplots(figsize=(8, 8))

fig.patch.set_facecolor('#121212')
ax.set_facecolor('#121212')

wedges, texts, autotexts = ax.pie(
    portfolio_df['Value'],
    labels=portfolio_df.index,
    autopct='%1.1f%%',
    pctdistance=0.75
)

for text in texts:
    text.set_color('white')

ax.set_title("Portfolio Allocation", color='orange', fontsize=18, fontweight='bold')

plt.show()