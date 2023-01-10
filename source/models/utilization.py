from dataclasses import dataclass, field

__all__ = ["Utilization"]


@dataclass
class Utilization:
    core: int | str
    usage: list[list[float]] | list[float]
    per: int = field(default=3600)
