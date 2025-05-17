from abc import ABC, abstractmethod
from typing import Any
from tradingsuite.signal import Signal

class Alpha(ABC):
    """
    Abstract base class for implementing trading strategies (alpha models).

    This class defines the interface that all trading strategies must implement.
    Each strategy must provide methods for updating market data and computing
    trading signals.

    Attributes:
        None

    Raises:
        NotImplementedError: If a concrete class does not implement all abstract methods

    AUTHOR: Jack Regan
    """
    @abstractmethod
    def update(self) -> None:
        """
        Ingest new market data

        Returns:
            None
        """
        pass

    @abstractmethod
    def compute_signal(self) -> Signal:
        """
        Generate trading signals based on current market data.

        Returns:
            A trading signal. The exact type depends on the concrete implementation.
        """
        pass