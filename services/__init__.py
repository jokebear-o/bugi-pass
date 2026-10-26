"""응용 계층 서비스 (COMP-02 ~ COMP-07)

- query_parser.py   COMP-02 질의 해석기 (LLM)        — 반복 2
- place_search.py   COMP-03 사용처 검색기            — 반복 1
- course_builder.py COMP-04 코스 생성기 (ODsay)      — 반복 2
- budget.py         COMP-05 예산 계산기              — 초기 버전 완료
- explainer.py      COMP-06 설명 생성기 (RAG)        — 반복 3
- receipt_reader.py COMP-07 사진 인식기 (VLM)        — 반복 3

규칙: 서비스는 외부 API를 직접 호출하지 않고 adapters/ 를 거친다 (NFR-004).
"""
