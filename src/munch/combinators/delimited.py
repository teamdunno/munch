from ..meta.types import MunchParser, MunchResult
from ..combinators.between import between

def delimited(begin: MunchParser, middle: MunchParser, end: MunchParser) -> MunchParser:
    def wrapped(input: str) -> MunchResult:
        ok, _, inside = between(begin, end)(input)
        return middle(inside) if ok else (False, input, "")

    return wrapped
