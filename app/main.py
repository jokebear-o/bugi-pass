"""COMP-01 화면 모듈 (Streamlit) — 초기 화면. 실행: streamlit run app/main.py"""
import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))
from services.budget import simulate_budget  # noqa: E402

st.set_page_config(page_title="부기패스", page_icon="🚌")
st.title("부기패스")
st.caption("부산 사용처·대중교통 AI 예산 안내 — 개발 중 (v0.2)")

st.subheader("UI-01 코스 요청")
st.text_area("원하는 코스를 한 문장으로 말해 주세요",
             placeholder="토요일에 서면에서 출발해서 국밥 먹고 근처 한 곳 더, 3만 원 안에서",
             disabled=True)
st.info("AI 조건 추출(FR-001)은 반복 2에서 연결됩니다.")

st.subheader("예산 시뮬레이션 미리보기 (FR-004)")
budget = st.number_input("보유 예산(원)", min_value=0, value=30000, step=1000)
c1, c2 = st.columns(2)
spend1 = c1.number_input("사용처 ① 결제액", min_value=0, value=9000, step=500)
spend2 = c2.number_input("사용처 ② 결제액", min_value=0, value=3000, step=500)
fare = st.number_input("교통요금 합계(원)", min_value=0, value=3100, step=100)

result = simulate_budget(int(budget), [int(spend1), int(spend2)], [int(fare)])
label = "초과" if result.is_over() else "잔액"
st.metric(label, f"{abs(result.remain):,}원",
          help=f"결제 {result.spend_total:,}원 + 교통 {result.fare_total:,}원")

st.caption("데이터 출처: 부산광역시 공공데이터포털 · ODsay · © OpenStreetMap contributors")
