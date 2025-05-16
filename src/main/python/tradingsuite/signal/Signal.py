from dataclasses import dataclass
from DateTime import DateTime

@dataclass(frozen=True)
class Signal:
    side: str
    timestamp: DateTime = DateTime.now()
    asset_id: str
    source: str
    confidence: float