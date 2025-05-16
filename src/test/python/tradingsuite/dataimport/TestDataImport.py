import unittest
from pathlib import Path
import pandas as pd
from tradingsuite.dataimport import DataImport

PROJECT_ROOT = "src/test/resources/tradingsuite/"
TEST_TICKER_CSV = PROJECT_ROOT + "test_tickers.csv"
NEGATIVE_TEST_TICKER_CSV = PROJECT_ROOT + "negative_test_tickers.csv"
PICKLE_WRITE_PATH = PROJECT_ROOT + "historicaldata/"

class TestDataImport(unittest.TestCase):
    """Tests data import class"""
    def test_positive_import_from_test_csv(self):

        start = "2010-01-01"
        end = "2010-12-31"
        DataImport.import_historical_data(TEST_TICKER_CSV, start, end, PICKLE_WRITE_PATH)

        for ticker in ["AAPL"]:
            pickle_file = Path(PICKLE_WRITE_PATH + f"{ticker}.pkl")
            self.assertTrue(pickle_file.exists(), f"Pickle file for {ticker} does not exist")

            # Optional: Assert file is not empty
            self.assertGreater(pickle_file.stat().st_size, 0, f"Pickle file for {ticker} is empty")

            # Optional: Load and check it's a DataFrame with rows
            df = pd.read_pickle(pickle_file)
            self.assertFalse(df.empty, f"Pickle DataFrame for {ticker} is empty")
    
    def test_negative_import_from_test_csv(self):
        start = "2010-01-01"
        end = "2010-12-31"

        with self.assertRaises(KeyError):
            DataImport.import_historical_data(NEGATIVE_TEST_TICKER_CSV, start, end, PICKLE_WRITE_PATH)



if __name__ == "__main__":
    unittest.main()