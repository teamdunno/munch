from ..meta.types import MunchParser, MunchResult


def all_until(delimiter: MunchParser) -> MunchParser:
    def wrapped(input: str) -> MunchResult:
        collected = ""
        remaining = input

        while True:
            matched, new_remaining, _ = delimiter(remaining)

            if matched:
                return (
                    True,
                    new_remaining,
                    collected
                )

            if len(remaining) == 0:
                return (
                    False,
                    remaining,
                    collected
                )

            collected += remaining[0]
            remaining = remaining[1:]

    return wrapped
