from ..meta.types import MunchParser


def opt(parser: MunchParser):
    def wrapped(input: str):
        try:
            result = parser(input)

            if not result[0]:
                return True, input, ""
            else:
                return True, result[1], result[2]
        except Exception:
            return True, input, ""

    return wrapped
