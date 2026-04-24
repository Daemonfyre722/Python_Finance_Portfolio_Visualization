# Portfolio Allocation Visualization

This project fetches real-time stock data for a selected portfolio and visualizes the allocation of investments using a pie chart. The goal is to represent how capital is distributed across different assets in a simple and visually clear format.


## What this project does

The script retrieves the latest stock prices, calculates the total value of each holding based on the number of shares, and visualizes the portfolio distribution using a pie chart.



## Tools and libraries used

* Python
* yfinance – for fetching market data
* pandas – for data manipulation and calculations
* matplotlib – for visualization

## How it works

* Define a list of stock tickers and corresponding share quantities
* Download recent stock price data using Yahoo Finance
* Extract the latest closing price for each stock
* Multiply price by number of shares to compute total value
* Store results in a structured portfolio table
* Calculate total portfolio value
* Visualize allocation using a pie chart

## Output

* A printed table showing:

  * Latest stock price
  * Number of shares held
  * Total value per stock

* A pie chart showing:

  * Percentage allocation of each stock in the portfolio
  * Visual representation of diversification



## Visualization style

* Dark-themed background for better contrast
* Colored pie chart segments representing each stock
* Percentage labels displayed inside the chart


## Purpose

This project was built to practice working with financial data in Python, improve data analysis skills using pandas, and learn basic  visualization techniques.




