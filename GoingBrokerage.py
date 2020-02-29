import alpha_vantage
import matplotlib
import mplfinance as mpf

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Your key here
key = 'TVQWKKX9Z8RFJSYD'


def run():
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    # Get the data, returns a tuple
    # aapl_data is a pandas dataframe, aapl_meta_data is a dict
    data, meta_data = ts.get_intraday(symbol='AMZN',interval='1min',outputsize='compact',)
    RSIdata = ti.get_rsi(symbol='AMZN', interval='1min',time_period=10,series_type='close')
    # aapl_sma is a dict, aapl_meta_sma also a dict
    sma, meta_sma = ti.get_sma(symbol='AMZN')


    # Visualization
    # figure(num=1, figsize=(18, 6), dpi=100, facecolor='w', edgecolor='k')
    # data['4. close'].plot()
    # plt.tight_layout()
    # plt.grid()
    # plt.show()
    # plt.subplot(555)
    print(data)
    mpf.plot(data)
    mpf.tight_layout()
    mpf.ylabel('Price(USD$)')
    mpf.xlabel('Minutes')
    mpf.title('AMZN')
    mpf.grid()
    mpf.show()

if __name__ == "__main__":
    run()
