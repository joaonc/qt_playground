import platform
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable


class OsName(str, Enum):  # Can be `StrEnum` on python 3.11+
    Windows = 'Windows'
    Linux = 'Linux'
    MacOS = 'Darwin'

    @classmethod
    def from_system_name(cls, name: str) -> 'OsName':
        return cls._value2member_map_[name]  # type: ignore

    @classmethod
    def this(cls):
        return cls.from_system_name(platform.system())


@dataclass
class OsData:
    """Data associated with OS platforms."""

    data: Any
    os_include: Iterable[OsName] = field(default_factory=list)
    os_exclude: Iterable[OsName] = field(default_factory=list)

    def __post_init__(self):
        overlap = set(self.os_include).intersection(self.os_exclude)
        if overlap:
            raise ValueError(
                f'The following values cannot be both included and excluded: {overlap}'
            )
