import yfinance as yf
import pandas as pd
import pickle
import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

"""
Import loads in historical market data from a third party API and stores the data as a pickle.

Attributes:


Raises:


"""
PROJECT_ROOT = "src/main/resources/tradingsuite/"
TICKER_SYMBOL_CSV_PATH = PROJECT_ROOT + "sp_500_tickers.csv"
PICKLE_WRITE_PATH = PROJECT_ROOT + "historicaldata/"

    
def import_historical_data(ticker, start_date, end_date, write_path):
    
    tickers_to_collect = pd.read_csv(ticker)
    tickers_list = tickers_to_collect['ticker'].tolist()

    for symbol in tickers_list:
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(start=start_date, end=end_date)
            if not hist.empty:
                hist.to_pickle(write_path + f"{symbol}.pkl")
                logging.info(f"Pickled {symbol}")
            else:
                logging.info(f"No data for {symbol}")
        except Exception as e:
            logging.error(f"Failed to download {symbol}: {e}")
    logging.info(f"The historical market data was successfully saved to {PICKLE_WRITE_PATH}")

if __name__ == "__main__":
    start = "2010-01-01"
    end = "2020-12-31"
    import_historical_data(TICKER_SYMBOL_CSV_PATH, start, end, PICKLE_WRITE_PATH)

