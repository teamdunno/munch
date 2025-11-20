from ..meta.types import MunchParser, MunchResult


def tag(tag: str) -> MunchParser:
    def wrapped(input: str) -> MunchResult:
        length = len(tag)
        return (
            input.startswith(tag),
            input[length:],
            tag
        )

    return wrapped
