from ..meta.types import MunchResult


def digit(input: str) -> MunchResult:
    if len(input) == 0:
        return (
            False,
            input,
            input
        )

    return (
        input[0].isdigit(),
        input[1:],
        input[0]
    )
