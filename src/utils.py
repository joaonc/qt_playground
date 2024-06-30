import platform
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable


class OsName(str, Enum):  # Can be `StrEnum` on python 3.11+
    """Enum to strongly type the results of ``platform.system()``."""

    Windows = 'Windows'
    Linux = 'Linux'
    MacOS = 'Darwin'

    @classmethod
    def from_system_name(cls, name: str) -> 'OsName':
        return cls._value2member_map_[name]  # type: ignore

    @classmethod
    def this(cls) -> 'OsName':
        return cls.from_system_name(platform.system())


@dataclass
class OsData:
    """Data associated with OS platforms."""

    data: Any
    os_include: Iterable[OsName] = field(default_factory=list)
    """
    OS's the data applies to.

    Empty means applies to all OS's.
    """
    os_exclude: Iterable[OsName] = field(default_factory=list)
    """
    OS's the data applies to.

    Empty means there are no OS restrictions and applies to all OS's.
    """

    def __post_init__(self):
        overlap = set(self.os_include).intersection(self.os_exclude)
        if overlap:
            raise ValueError(
                f'The following values cannot be both included and excluded: {overlap}'
            )

    def applies(self, os_name: OsName | None = None) -> bool:
        """Whether this instance applies to the current platform."""
        os_name = os_name or OsName.this()
        if self.os_include and os_name not in self.os_include:
            return False
        if self.os_exclude and os_name in self.os_exclude:
            return False
        return True
