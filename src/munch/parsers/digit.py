from ..meta.types import MunchResult


def digit(input: str) -> MunchResult:
    if len(input) == 0:
        return (
            False,
            input,
            input
        )

    if not input[0].isdigit():
        return (
            False,
            input,
            ""
        )

    return (
        True,
        input[1:],
        input[0]
    )
