import pandas as pd

x = pd.read_html('https://finviz.com/quote.ashx?t=MSFT')
print(x)