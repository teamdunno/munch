from ..meta.types import MunchParser, MunchResult


def tag(tag: str) -> MunchParser:
    def wrapped(input: str) -> MunchResult:
        length = len(tag)

        if not input.startswith(tag):
            return (False, input, "")

        return (
            True,
            input[length:],
            tag
        )

    return wrapped
