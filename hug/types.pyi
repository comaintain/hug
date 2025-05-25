from abc import abstractmethod
from decimal import Decimal
from uuid import UUID

from _typeshed import Incomplete

class ValidationError(Exception): ...

class Type:
    _hug_type: bool = True
    _sub_type: Incomplete = None
    _accept_context: bool = False

    def __init__(self) -> None: ...
    @abstractmethod
    def __call__(self, value: object) -> object: ...

def create(
    doc: str | None = None,
    error_text: str | None = None,
    exception_handlers=...,
    extend=...,
    chain: bool = True,
    auto_instance: bool = True,
    accept_context: bool = False,
): ...
def accept(
    kind,
    doc: str | None = None,
    error_text: str | None = None,
    exception_handlers=...,
    accept_context: bool = False,
): ...

# Pretend these are actual types (instead of `Type` objects) to get better type checking & IDE behavior
number = int
float_number = float
decimal = Decimal
boolean = bool
uuid = UUID
multiple = list
smart_boolean = bool
inline_dictionary = dict[str, str]
comma_separated_list = list[str]
json = object
text = str

class Text(Type):
    def __call__(self, value): ...

class SubTyped(type):
    def __getitem__(cls, sub_type): ...

class Multiple(Type, metaclass=SubTyped):
    def __call__(self, value): ...

class DelimitedList(Type, metaclass=SubTyped):
    using: Incomplete
    def __init__(self, using: str = ",") -> None: ...
    def __call__(self, value): ...

class SmartBoolean(Incomplete):
    def __call__(self, value): ...

class InlineDictionary(Type, metaclass=SubTyped):
    key_type: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, string): ...

class OneOf(Type):
    values: Incomplete
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class Mapping(OneOf):
    value_map: Incomplete
    values: Incomplete
    def __init__(self, value_map) -> None: ...
    def __call__(self, value): ...

class JSON(Type):
    def __call__(self, value): ...

class Multi(Type):
    types: Incomplete
    def __init__(self, *types) -> None: ...
    def __call__(self, value): ...

class InRange(Type):
    lower: Incomplete
    upper: Incomplete
    convert: Incomplete
    def __init__(self, lower, upper, convert=...) -> None: ...
    def __call__(self, value): ...

class LessThan(Type):
    limit: Incomplete
    convert: Incomplete
    def __init__(self, limit, convert=...) -> None: ...
    def __call__(self, value): ...

class GreaterThan(Type):
    minimum: Incomplete
    convert: Incomplete
    def __init__(self, minimum, convert=...) -> None: ...
    def __call__(self, value): ...

class Length(Type):
    lower: Incomplete
    upper: Incomplete
    convert: Incomplete
    def __init__(self, lower, upper, convert=...) -> None: ...
    def __call__(self, value): ...

class ShorterThan(Type):
    limit: Incomplete
    convert: Incomplete
    def __init__(self, limit, convert=...) -> None: ...
    def __call__(self, value): ...

class LongerThan(Type):
    limit: Incomplete
    convert: Incomplete
    def __init__(self, limit, convert=...) -> None: ...
    def __call__(self, value): ...

class CutOff(Type):
    limit: Incomplete
    convert: Incomplete
    def __init__(self, limit, convert=...) -> None: ...
    def __call__(self, value): ...

class Chain(Type):
    types: Incomplete
    def __init__(self, *types) -> None: ...
    def __call__(self, value): ...

class Nullable(Chain):
    types: Incomplete
    def __init__(self, *types) -> None: ...
    def __call__(self, value): ...

class TypedProperty:
    name: Incomplete
    type_func: Incomplete
    def __init__(self, name, type_func) -> None: ...
    def __get__(self, instance, cls): ...
    def __set__(self, instance, value) -> None: ...
    def __delete__(self, instance) -> None: ...

class NewTypeMeta(type):
    def __init__(cls, name, bases, nmspc) -> None: ...

class Schema(metaclass=NewTypeMeta):
    def __new__(cls, json, *args, **kwargs): ...
    def __init__(self, json, force: bool = False) -> None: ...

class MarshmallowInputSchema(Type):
    schema: Incomplete
    def __init__(self, schema) -> None: ...
    def __call__(self, value, context): ...

class MarshmallowReturnSchema(Type):
    schema: Incomplete
    def __init__(self, schema) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, context) -> None: ...
    def __call__(self, value): ...

delimited_list = DelimitedList
one_of = OneOf
mapping = Mapping
multi = Multi
in_range = InRange
less_than = LessThan
greater_than = GreaterThan
length = Length
shorter_than = ShorterThan
longer_than = LongerThan
cut_off = CutOff
