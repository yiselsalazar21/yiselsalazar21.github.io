import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

df = pytrend.interest_by_region()
df.head(10)