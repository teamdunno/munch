from typing import Any, Callable

# (ok, input, result)
type MunchResult = tuple[bool, str, Any]

# fn (input: str) -> MunchResult
type MunchParser = Callable[[str], MunchResult]
