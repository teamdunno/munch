from ..meta.types import MunchParser


def many(parser: MunchParser) -> MunchParser:
    def wrapped(input: str):
        results = []
        rest = input

        while True:
            try:
                ok, new_rest, result = parser(rest)

                if not ok:
                    break
            except Exception:
                break

            results.append(result)
            rest = new_rest

        return True, rest, results

    return wrapped
