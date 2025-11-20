from ..meta.types import MunchResult, MunchParser
from ..parsers.all_until import all_until

def between(begin: MunchParser, end: MunchParser) -> MunchParser:
    def wrapped(input: str) -> MunchResult:
        matched_begin, remaining_after_begin, _ = begin(input)

        if not matched_begin:
            return False, input, ""

        end_is_there, before_end, delimited = all_until(end)(remaining_after_begin)
        if not end_is_there:
            return False, input, ""

        return True, before_end, delimited

    return wrapped
