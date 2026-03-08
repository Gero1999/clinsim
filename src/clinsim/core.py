"""Core simulation primitives."""

from __future__ import annotations


def simulate(seed: int | None = None) -> dict[str, int | None]:
    """Run a minimal simulation placeholder.

    Args:
        seed: Optional integer random seed.

    Returns:
        Basic simulation metadata.
    """
    return {"status": "initialized", "seed": seed}
