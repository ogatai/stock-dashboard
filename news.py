import pandas as pd
import os
from stock import get_stock_price

os.makedirs("data", exist_ok=True)

portfolio = [
    {"name": "NTT", "code": "9432.T", "quantity": 100, "buy_price": 150},
]

results = []

for item in portfolio:
    price = get_stock_price(item["code"])
    total_value = price * item["quantity"]
    profit = (price - item["buy_price"]) * item["quantity"]

    results.append({
        "銘柄": item["name"],
        "現在価格": price,
        "数量": item["quantity"],
        "評価額": total_value,
        "損益": profit
    })

df = pd.DataFrame(results)
df.to_csv("data/portfolio.csv", index=False, encoding="utf-8-sig")

print(df)

#ここから追加
import matplotlib.pyplot as plt

df.plot(x="銘柄", y="評価額", kind="bar")
plt.title("ポートフォリオ評価額")
plt.tight_layout()
plt.show()

