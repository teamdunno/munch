from ..meta.types import MunchResult


def letter(input: str) -> MunchResult:
    if len(input) == 0:
        return (
            False,
            input,
            input
        )

    return (
        input[0].isalpha(),
        input[1:],
        input[0]
    )
