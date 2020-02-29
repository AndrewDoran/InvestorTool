import alpha_vantage
import matplotlib
import mplfinance as mpf
import re
import sys
import requests

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Your key here
key = 'TVQWKKX9Z8RFJSYD'

def fix_stonk_columns(data):
    # for key, value in dictionary:
    #     new_key = re.sub('[a-zA-Z]+', '*', key)
    #     dictionary[new_key] = dictionary.pop(key)
    #     print("old key: {}, new key: {}".format(key, new_key))
    # return dictionary
    # data.columns[0] = 'open'
    # data.columns[1] = 'high'
    # data.columns[2] = 'low'
    # data.columns[3] = 'close'
    # data.columns[4] = 'volume'
    data.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    }, inplace=True)
    print(data.columns)


def run():
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    # # Get the data, returns a tuple
    # # aapl_data is a pandas dataframe, aapl_meta_data is a dict
    data, meta_data = ts.get_intraday(symbol='AMZN', interval='1min', outputsize='compact')
    fix_stonk_columns(data)

    # RSIdata = ti.get_rsi(symbol='AMZN', interval='1min',time_period=10,series_type='close')
    # # aapl_sma is a dict, aapl_meta_sma also a dict
    # sma, meta_sma = ti.get_sma(symbol='AMZN')
    # response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=5min&outputsize=full&apikey=TVQWKKX9Z8RFJSYD")
    # print(response)
    # Visualization
    # figure(num=1, figsize=(18, 6), dpi=100, facecolor='w', edgecolor='k')
    # data['4. close'].plot()
    # plt.tight_layout()
    # plt.grid()
    # plt.show()
    # plt.subplot(555)
    # print('>>>')
    # trim_stonk_col_names(data)
    # print(data)

    mpf.plot(data,type='candle', mav=(9,26), volume=True)
    mpf.tight_layout()
    mpf.ylabel('Price(USD$)')
    mpf.xlabel('Minutes')
    mpf.title('AMZN')
    mpf.grid()
    mpf.show()

if __name__ == "__main__":
    run()
