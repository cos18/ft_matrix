from beartype import beartype, typing
from beartype.typing import List
from copy import deepcopy

T = typing.TypeVar('T')


@beartype
class Vector:
    def __init__(self, value: List[T]):
        self._value = deepcopy(value) if value else list()

    def __len__(self) -> int:
        """Dunder method to return the size of a vector"""
        return len(self._value)

    def __str__(self) -> str:
        """Dunder method to stringify object"""
        return str(self._value)

    def to_matrix(self) -> None:
        pass
