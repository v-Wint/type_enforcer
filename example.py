from typing import List, Union, Optional, Any, Tuple, Dict, Callable, TypeVar, Generic
from type_enforcer import annotated


@annotated(enforced=True)
def add(a: int, b: int) -> int:
    return a + b


@annotated(enforced=True)
def stringify(value: Union[int, float, str]) -> str:
    return str(value)


@annotated(enforced=True)
def maybe_multiply(value: Optional[int], multiplier: int) -> Optional[int]:
    if value is None:
        return None
    return value * multiplier


@annotated(enforced=True)
def sum_list(numbers: List[int]) -> int:
    return sum(numbers)


@annotated(enforced=True)
def get_coordinates() -> Tuple[float, float]:
    return 40.7128, -74.0060


@annotated(enforced=True)
def phonebook_entry(name: str, phone: str) -> Dict[str, str]:
    return {"name": name, "phone": phone}


@annotated(enforced=True)
def execute_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


T = TypeVar('T')


class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


@annotated(enforced=True)
def print_any(value: Any) -> None:
    print(value)


@annotated(enforced=True)
def complex_function(data: List[Dict[str, Union[int, List[Optional[str]]]]]) -> None:
    for item in data:
        print(item)


@annotated(enforced=True)
def flatten(lst: List[Union[int, List['flatten']]]) -> List[int]:
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
