import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def get_company_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    financials = stock.financials
    
    return {
        'name': info['longName'],
        'sector': info['sector'],
        'price': info['currentPrice'],
        'market_cap': info['marketCap'],
        'pe_ratio': info['trailingPE'],
        'dividend_yield': info['dividendYield'] if 'dividendYield' in info else None,
        'revenue': financials.loc['Total Revenue'].values[0],
        'net_income': financials.loc['Net Income'].values[0],
    }

def plot_dashboard(data):
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(3, 3, figure=fig)
    
    # Company name and sector
    fig.text(0.5, 0.95, f"{data['name']} ({data['sector']})", ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Price and Market Cap
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.text(0.5, 0.8, f"Price: ${data['price']:.2f}", ha='center', va='center', fontsize=12)
    ax1.text(0.5, 0.2, f"Market Cap: ${data['market_cap']:,.0f}", ha='center', va='center', fontsize=12)
    ax1.axis('off')
    
    # PE Ratio and Dividend Yield
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.text(0.5, 0.8, f"P/E Ratio: {data['pe_ratio']:.2f}", ha='center', va='center', fontsize=12)
    if data['dividend_yield']:
        ax2.text(0.5, 0.2, f"Dividend Yield: {data['dividend_yield']:.2%}", ha='center', va='center', fontsize=12)
    else:
        ax2.text(0.5, 0.2, "Dividend Yield: N/A", ha='center', va='center', fontsize=12)
    ax2.axis('off')
    
    # Revenue and Net Income
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.text(0.5, 0.8, f"Revenue: ${data['revenue']:,.0f}", ha='center', va='center', fontsize=12)
    ax3.text(0.5, 0.2, f"Net Income: ${data['net_income']:,.0f}", ha='center', va='center', fontsize=12)
    ax3.axis('off')
    
    # Historical price chart
    ax4 = fig.add_subplot(gs[1:, :])
    stock = yf.Ticker(ticker)
    history = stock.history(period="1y")
    ax4.plot(history.index, history['Close'])
    ax4.set_title('1 Year Price History')
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Price')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter company ticker symbol: ")
    company_data = get_company_data(ticker)
    plot_dashboard(company_data)