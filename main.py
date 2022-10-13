import yfinance as yf
import pandas as pd
import utils

data = yf.download("^NSEI",period="1d",interval="5m")
# print(data.tail(4))


data['ema'] = utils.ema_5(data)
print(data.ema.tail(5))