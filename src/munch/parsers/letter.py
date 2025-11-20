from ..meta.types import MunchResult


def letter(input: str) -> MunchResult:
    if len(input) == 0:
        return (
            False,
            input,
            ""
        )

    if not input[0].isalpha():
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
