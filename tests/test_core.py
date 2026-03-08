from clinsim import simulate


def test_simulate_default() -> None:
    result = simulate()
    assert result["status"] == "initialized"
    assert result["seed"] is None


def test_simulate_with_seed() -> None:
    result = simulate(seed=42)
    assert result == {"status": "initialized", "seed": 42}
