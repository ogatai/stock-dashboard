import os

# dataフォルダがなければ作る
os.makedirs("data", exist_ok=True)

from stock import get_stock_price
import pandas as pd

# 企業株・ETF・投資信託
codes = {
    "トヨタ": "7203.T",
    "ソニー": "6758.T",
    "三菱UFJ": "8306.T",
    "NTT": "9432.T",

    # ETF
    "S&P500 ETF": "SPY",
    "NASDAQ ETF": "QQQ",

    # 投資信託代替
    "eMAXIS Slim 国内株式(TOPIX)": "1306.T",
    "ニッセイSOX指数（代替ETF）": "SOXX",
    "SBI ゴールド（代替ETF）": "GLD"
}


results = []

for name, code in codes.items():
    price = get_stock_price(code)

    results.append({
        "name": name,
        "code": code,
        "price": price
    })

df = pd.DataFrame(results)

print(df)

df.to_csv("data/portfolio.csv", index=False, encoding="utf-8-sig")
