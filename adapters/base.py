"""COMP-08 외부 연동 어댑터 인터페이스 (NFR-004, SDD 4.1 Class Diagram)

서비스는 아래 인터페이스에만 의존하고, 실제 API 구현체는 교체 가능하게 둔다.
단위 시험에서는 Mock 구현체를 사용한다.
"""
from abc import ABC, abstractmethod


class AIService(ABC):
    """LLM/VLM 호출 추상화 (API-104). 시간 제한 10초, 실패 시 1회 재시도."""

    @abstractmethod
    def complete(self, prompt: str, schema: dict | None = None, image: bytes | None = None) -> dict | str:
        ...


class RouteClient(ABC):
    """대중교통 경로 조회 (API-101, ODsay)."""

    @abstractmethod
    def route(self, from_xy: tuple[float, float], to_xy: tuple[float, float]) -> dict:
        """반환: {"minutes": int, "fare": int, "transfers": int, "path": list}"""
        ...


class GeoClient(ABC):
    """업소명·주소 → 좌표 변환 (API-102, Kakao Local)."""

    @abstractmethod
    def geocode(self, keyword: str) -> tuple[float, float] | None:
        ...
