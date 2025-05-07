# title: player_portfolio.py

class PlayerPortfolio:
    def __init__(self, starting_cash=10000):
        self.cash = starting_cash
        self.holdings = {}  # { 'Ticker': shares_owned }
        self.trades = []    # For tracking and plotting trades
        self.history = []   # For tracking portfolio value over time

    def buy(self, ticker, price, quantity, day=None):
        cost = price * quantity
        if cost > self.cash:
            print(f"Not enough cash to buy {quantity} shares of {ticker}.")
            return False
        else:
            self.cash -= cost
            self.trades.append({'type': 'buy', 'ticker': ticker, 'price': price, 'day': day})
            self.holdings[ticker] = self.holdings.get(ticker, 0) + quantity
            print(f"Bought {quantity} shares of {ticker} at ${price:.2f}.")
            return True

    def sell(self, ticker, price, quantity, day=None):
        if self.holdings.get(ticker, 0) < quantity:
            print(f"Not enough shares to sell {quantity} shares of {ticker}.")
            return False
        else:
            self.cash += price * quantity
            self.trades.append({'type': 'sell', 'ticker': ticker, 'price': price, 'day': day})
            self.holdings[ticker] -= quantity
            print(f"Sold {quantity} shares of {ticker} at ${price:.2f}.")
            return True


    def portfolio_value(self, current_prices):
        """
        Calculate total portfolio value (cash + holdings market value).
        
        Parameters:
        - current_prices (dict): { 'Ticker': latest_price }
        
        Returns:
        - total_value (float)
        """
        holdings_value = 0
        for ticker, shares in self.holdings.items():
            price = current_prices.get(ticker, 0)
            holdings_value += shares * price
        total_value = self.cash + holdings_value
        return total_value


    def show_holdings(self):
        """
        Print a neat summary of holdings.
        """
        print("Current Holdings:")
        if not self.holdings:
            print("  None")
        else:
            for ticker, shares in self.holdings.items():
                print(f"  {ticker}: {shares} shares")
        print(f"Cash Balance: ${self.cash:.2f}")
