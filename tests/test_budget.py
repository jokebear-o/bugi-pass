"""TC-004 / TC-011 예산 계산 시험 (FR-004, NFR-002)"""
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from services.budget import simulate_budget  # noqa: E402


def test_remain_within_budget():
    r = simulate_budget(30000, [9000, 3000], [1550, 1550])
    assert (r.spend_total, r.fare_total, r.remain) == (12000, 3100, 14900)
    assert not r.is_over()


def test_over_budget_is_negative():
    r = simulate_budget(10000, [9000], [1550])
    assert r.remain == -550
    assert r.is_over()


def test_negative_input_rejected():
    with pytest.raises(ValueError):
        simulate_budget(-1, [1000], [0])
