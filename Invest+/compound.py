def compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    
    :param principal: Initial principal balance
    :param rate: Annual interest rate (as a decimal)
    :param time: Number of years
    :param n: Number of times interest is compounded per year (default is 1)
    :return: Final amount after applying compound interest
    """
    amount = principal * (1 + rate/n)**(n*time)

    return amount

# Example usage
principal = 100  # Initial investment
rate = 0.15       # 5% annual interest rate
time = 20          # 5 years
n = 1            # Compounded monthly

final_amount = compound_interest(principal, rate, time, n)
interest_earned = final_amount - principal

print(f"Final amount: ${final_amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")

import matplotlib.pyplot as plt

# 添加绘图功能
def plot_compound_interest(principal, rate, years, n=1):
    amounts = [compound_interest(principal, rate, t, n) for t in range(1, years+1)]
    
    plt.figure(figsize=(12, 8))
    bars = plt.bar(range(1, years+1), amounts, color='skyblue')
    plt.title(f'Compound Interest Over {years} Years')
    plt.xlabel('Years')
    plt.ylabel('Total Amount ($)')
    plt.xticks(range(1, years+1))
    
    # 调整y轴的范围，为标签留出空间
    plt.ylim(0, max(amounts) * 1.1)
    
    # 在柱状图上方添加标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'${height:.2f}',
                 ha='center', va='bottom', rotation=45)
    
    plt.tight_layout()
    plt.show()

# 使用示例
if __name__ == "__main__":
    principal = 100  # 初始投资
    rate = 0.12       # 5% 年利率
    years = 10        # 10年
    n = 1            # 每月复利

    plot_compound_interest(principal, rate, years, n)