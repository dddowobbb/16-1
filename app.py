import streamlit as st
import random
import matplotlib.pyplot as plt

# 세션 상태 초기화
default_keys = {
    "step": 0,
    "industry": "",
    "company_name": "",
    "strategy": "",
    "event": "",
    "revenue": [],
    "industry_confirmed": False
}

for key, val in default_keys.items():
    if key not in st.session_state:
        st.session_state[key] = val
st.markdown("""
<style>
    .block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    header, footer, .viewerBadge_container__1QSob {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# 상단 제목
st.title("📈 경영 시뮬레이터: 나만의 회사를 만들어보자!")

# CEO 이미지 삽입
st.image(
    "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png",
    use_container_width=True
)

# Step 0: 업종 선택
if st.session_state.step == 0:
    st.subheader("Step 1: 업종을 선택하세요 🔍")

    if not st.session_state.industry_confirmed:
        industries = [
            "💻 IT 스타트업",
            "🌱 친환경 제품",
            "🎮 게임 개발사",
            "👗 패션 브랜드",
            "🍔 푸드테크",
            "🛒 글로벌 전자상거래"
        ]
        selected = st.selectbox("회사 업종을 선택해주세요", industries)
        if st.button("업종 확정"):
            st.session_state.industry = selected
            st.session_state.industry_confirmed = True
            st.success(f"선택된 업종: {selected}")
    else:
        st.info(f"✅ 선택된 업종: **{st.session_state.industry}**")
        if st.button("다음 ▶️"):
            st.session_state.step = 1

# Step 1: 회사 이름 입력
elif st.session_state.step == 1:
    st.subheader("Step 2: 회사 이름을 지어주세요 🏢")
    company_input = st.text_input("원하는 회사 이름을 입력하세요", max_chars=20)

    if st.button("회사 이름 확정"):
        if company_input.strip() == "":
            st.warning("회사 이름을 입력해주세요!")
        else:
            st.session_state.company_name = company_input.strip()
            st.success(f"'{st.session_state.company_name}'이(가) 등록되었습니다!")

    if st.session_state.company_name:
        if st.button("다음 ▶️"):
            st.session_state.step = 2

# Step 2: 전략 선택
elif st.session_state.step == 2:
    st.subheader("Step 3: 경영 전략을 선택하세요 🎯")
    strategy = st.radio("전략 선택", [
        "🔬 연구개발(R&D)에 투자하여 기술 선도",
        "📢 마케팅을 강화하여 브랜드 인지도 상승",
        "🏭 생산 효율화를 통해 원가 절감",
        "🌐 해외 시장 진출 확대"
    ])

    if st.button("전략 확정"):
        st.session_state.strategy = strategy
        st.success(f"선택된 전략: {strategy}")

    if st.session_state.strategy:
        if st.button("다음 ▶️"):
            st.session_state.step = 3

# Step 3: 전략 결과
elif st.session_state.step == 3:
    st.subheader("Step 4: 전략 결과 📊")
    st.write(f"**{st.session_state.industry}** 업종의 **'{st.session_state.company_name}'** 회사는")
    st.write(f"**{st.session_state.strategy}** 전략을 채택하였습니다.")
    st.write("전략이 적용되어 회사의 기반이 강화되고 있습니다.")

    if st.button("다음 ▶️"):
        st.session_state.step = 4

# Step 4: 이벤트 발생
elif st.session_state.step == 4:
    st.subheader("Step 5: 예기치 못한 사건 발생 ⚠️")

    all_events = {
        "💻 IT 스타트업": [
            ("🌟 투자 유치 성공!", 1.3),
            ("💥 서버 보안 사고 발생", 0.7),
            ("🤖 AI 기술 특허 확보", 1.25),
            ("📉 경쟁 서비스에 밀림", 0.8),
        ],
        "🌱 친환경 제품": [
            ("🌿 정부의 친환경 보조금 수령", 1.2),
            ("🚫 환경단체 비판 보도", 0.75),
            ("🌎 해외 친환경 박람회 수상", 1.15),
            ("💸 생산 원가 상승", 0.85),
        ],
        "🎮 게임 개발사": [
            ("🔥 신작 게임 대히트!", 1.4),
            ("🐞 게임 내 버그로 유저 이탈", 0.6),
            ("🎮 인기 스트리머와 콜라보", 1.2),
            ("⏳ 출시 연기 논란", 0.8),
        ],
        "👗 패션 브랜드": [
            ("👠 인플루언서 협업 성공", 1.2),
            ("📉 트렌드 미스", 0.75),
            ("📸 해외 런웨이 초청", 1.15),
            ("🏭 생산 차질", 0.85),
        ],
        "🍔 푸드테크": [
            ("🥩 대체육 이슈로 언론 집중", 1.3),
            ("⚠️ 식품 안정성 논란", 0.7),
            ("🥗 비건 인플루언서 리뷰 호평", 1.2),
            ("💰 공급망 문제", 0.8),
        ],
        "🛒 글로벌 전자상거래": [
            ("🌐 해외시장 확장 성공", 1.25),
            ("🚚 물류대란 발생", 0.7),
            ("🛍️ 대형 쇼핑 이벤트 흥행", 1.3),
            ("📦 반품 증가로 손실 발생", 0.8),
        ]
    }

    if not st.session_state.event:
        events = all_events.get(st.session_state.industry, [])
        if events:
            st.session_state.event = random.choice(events)

    event_text, multiplier = st.session_state.event
    st.info(f"이벤트 발생: **{event_text}**")

    if st.button("다음 ▶️"):
        base = 100
        st.session_state.revenue = [
            int(base * multiplier * random.uniform(0.9, 1.1)) for _ in range(4)
        ]
        st.session_state.step = 5

# Step 5: 매출 시뮬레이션
elif st.session_state.step == 5:
    st.subheader("Step 6: 분기별 매출 실적 📈")
    quarters = ["1분기", "2분기", "3분기", "4분기"]

    fig, ax = plt.subplots()
    ax.plot(quarters, st.session_state.revenue, marker='o')
    ax.set_ylabel("매출 (억 원)")
    ax.set_title("분기별 매출 추이")
    st.pyplot(fig)

    if st.button("다음 ▶️"):
        st.session_state.step = 6

# Step 6: 최종 평가
elif st.session_state.step == 6:
    st.subheader("🏁 최종 경영 평가")
    total = sum(st.session_state.revenue)
    st.write(f"**'{st.session_state.company_name}'**의 연간 총 매출은 **{total}억 원**입니다.")

    if total >= 450:
        st.success("🎉 훌륭한 성과! 투자자와 언론의 찬사를 받았습니다.")
    elif total >= 350:
        st.info("👍 안정적인 운영! 더 큰 도약이 기대됩니다.")
    else:
        st.warning("📉 개선이 필요합니다. 전략 재설정과 리스크 관리가 중요합니다.")

    if st.button("🔁 처음부터 다시 시작"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
