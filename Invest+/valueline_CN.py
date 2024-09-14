import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 请替换为您的 tushare token
ts.set_token('a7e7d7a9980b028778da3fe47614a8e13aca49be193e1c5bff82baf2')
pro = ts.pro_api('a7e7d7a9980b028778da3fe47614a8e13aca49be193e1c5bff82baf2')

def get_company_data(stock_code):
    # 获取股票基本信息
    basic_info = pro.stock_basic(ts_code=stock_code, fields='name,industry,market,list_date')
    
    # 获取最新的每日指标
    daily_basic = pro.daily_basic(ts_code=stock_code, fields='close,pe,pb,total_mv,dv_ratio').iloc[0]
    
    # 获取最新的财务指标
    fina_indicator = pro.fina_indicator(ts_code=stock_code, period='20221231', fields='revenue,profit_dedt')
    
    return {
        'name': basic_info['name'].values[0],
        'industry': basic_info['industry'].values[0],
        'price': daily_basic['close'],
        'market_cap': daily_basic['total_mv'],
        'pe_ratio': daily_basic['pe'],
        'pb_ratio': daily_basic['pb'],
        'dividend_yield': daily_basic['dv_ratio'],
        'revenue': fina_indicator['revenue'].values[0],
        'net_income': fina_indicator['profit_dedt'].values[0],
    }

def plot_dashboard(data, stock_code):
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(3, 3, figure=fig)
    
    # Company name and industry
    fig.text(0.5, 0.95, f"{data['name']} ({data['industry']})", ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Price and Market Cap
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.text(0.5, 0.8, f"价格: ¥{data['price']:.2f}", ha='center', va='center', fontsize=12)
    ax1.text(0.5, 0.2, f"市值: ¥{data['market_cap']/100000000:.2f}亿", ha='center', va='center', fontsize=12)
    ax1.axis('off')
    
    # PE Ratio and PB Ratio
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.text(0.5, 0.8, f"市盈率: {data['pe_ratio']:.2f}", ha='center', va='center', fontsize=12)
    ax2.text(0.5, 0.2, f"市净率: {data['pb_ratio']:.2f}", ha='center', va='center', fontsize=12)
    ax2.axis('off')
    
    # Revenue and Net Income
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.text(0.5, 0.8, f"营收: ¥{data['revenue']/100000000:.2f}亿", ha='center', va='center', fontsize=12)
    ax3.text(0.5, 0.2, f"净利润: ¥{data['net_income']/100000000:.2f}亿", ha='center', va='center', fontsize=12)
    ax3.axis('off')
    
    # Historical price chart
    ax4 = fig.add_subplot(gs[1:, :])
    df = ts.pro_bar(ts_code=stock_code, adj='qfq', start_date='20220101')
    ax4.plot(pd.to_datetime(df['trade_date']), df['close'])
    ax4.set_title('近一年股价走势')
    ax4.set_xlabel('日期')
    ax4.set_ylabel('价格')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    stock_code = input("请输入股票代码（例如：000001.SZ）: ")
    company_data = get_company_data(stock_code)
    plot_dashboard(company_data, stock_code)