from ..meta.types import MunchResult
from ..parsers.digit import digit
from ..parsers.many import many
import builtins

def int(input: str) -> MunchResult:
    ok, input, digits = many(digit)(input)
    if not ok:
        return (
            False,
            input,
            0
        )

    strung = "".join(digits)
    try:
        number = builtins.int(strung)
    except Exception:
        return (
            False,
            input,
            0
        )
    
    return (
        True,
        input,
        number
    )

