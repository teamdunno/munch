from ..meta.types import MunchParser


def alt(*args: MunchParser) -> MunchParser:
    def wrapped(input: str):
        for parser in args:
            try:
                ok, rest, result = parser(input)

                if ok:
                    return True, rest, result
            except Exception:
                continue

        return False, input, None

    return wrapped
