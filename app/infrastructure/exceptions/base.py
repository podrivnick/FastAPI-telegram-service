from dataclasses import (
    asdict,
    dataclass,
)


@dataclass(frozen=True, eq=False)
class BaseApplicationException(Exception):
    @property
    def meta(self):
        return asdict(self)

    @property
    def message(self):
        return "Error in application"
