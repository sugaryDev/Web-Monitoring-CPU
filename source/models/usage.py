from dataclasses import dataclass

__all__ = ["Usage"]


@dataclass
class Usage:
    cores: int
    usage: str
    at: float
