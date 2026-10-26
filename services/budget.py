"""COMP-05 예산 계산기 (FR-004, NFR-002, API-004)

잔액 = 보유 예산 - Σ(사용처별 예상 결제액) - Σ(구간 교통요금)
초기 버전: 결제액·교통요금을 정수 목록으로 받는다. Course 객체 연동은 반복 2에서 진행.
"""
from dataclasses import dataclass


@dataclass
class BudgetResult:
    budget: int
    spend_total: int
    fare_total: int
    remain: int  # 음수이면 초과액

    def is_over(self) -> bool:
        return self.remain < 0


def simulate_budget(budget: int, spends: list[int], fares: list[int]) -> BudgetResult:
    """보유 예산에서 결제액과 교통요금을 차감한 결과를 반환한다."""
    values = [budget, *spends, *fares]
    if any(not isinstance(v, int) or v < 0 for v in values):
        raise ValueError("금액은 0 이상의 정수여야 합니다 (ERR-001)")
    spend_total = sum(spends)
    fare_total = sum(fares)
    return BudgetResult(budget, spend_total, fare_total, budget - spend_total - fare_total)
