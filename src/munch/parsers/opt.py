from ..meta.types import MunchParser


def opt(parser: MunchParser):
    def wrapped(input: str):
        try:
            result = parser(input)

            if not result[0]:
                return True, input, None
            else:
                return True, result[1], result[2]
        except Exception:
            return True, input, None

    return wrapped
