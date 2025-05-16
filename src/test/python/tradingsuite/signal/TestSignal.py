import unittest
from tradingsuite.signal.Signal import Signal
from DateTime import DateTime

class TestSignal(unittest.TestCase):
    """Tests for Signal data class"""
    def test_negative_type_error_initialize_signal(self):
        """Test value error"""
        with self.assertRaises(ValueError):
            Signal(side="hold", asset_id="AAPL", source="MA", confidence=0.8)

    def test_negative_value_error_initialize_signal(self):
        """Test value error"""
        with self.assertRaises(ValueError):
            Signal(side="buy", asset_id="AAPL", source="MA", confidence=20)

    def test_initialize_signal(self):
        """Test positive initialization"""
        signal = Signal("buy", "AAPL", "MA", 0.8)
        self.assertEqual(signal.side, "buy")
        self.assertEqual(signal.asset_id, "AAPL")
        self.assertEqual(signal.source, "MA")
        self.assertEqual(signal.confidence, 0.8)
        self.assertIsInstance(signal.timestamp, DateTime) 

if __name__ == '__main__':
    unittest.main()
    