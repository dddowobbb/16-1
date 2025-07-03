import streamlit as st
import random

st.set_page_config(layout="wide")

# 세션 상태 초기화
default_keys = {
    "step": 0,
    "industry": "",
    "company_name": "",
    "strategy": "",
    "situation": "",
    "industry_confirmed": False,
    "score": 0,
    "history": []
}
for key, val in default_keys.items():
    if key not in st.session_state:
        st.session_state[key] = val

# 적합한 전략 매핑
effective_strategies = {
    "⚠️ 대규모 고객 데이터 유출 발생": "보안 시스템 전면 재구축",
    "📈 갑작스러운 수요 폭증": "생산 라인 확장",
    "💸 원자재 가격 급등": "공급처 다변화",
    "🔥 경쟁사의 파산": "인재 채용 강화",
    "📉 주요 제품 매출 급감": "제품 리뉴얼",
    "🏆 대기업으로부터 투자 제안": "지분 일부 매각",
    "🌍 글로벌 시장 진출 기회": "현지화 전략"
}

# ✅ 스타일 정의
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
    background-color: #1a1a1a !important;
}
.container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    margin: 0;
    padding: 0;
    background-color: #1a1a1a;
}
.bg-image {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100vh;
    object-fit: cover;
    z-index: 0;
}
.speech-bubble {
    position: absolute;
    bottom: 8vh;
    left: 50%;
    transform: translateX(-50%);
    width: 70%;
    background: rgba(255, 255, 255, 0.95);
    padding: 25px 30px;
    border-radius: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    text-align: center;
    z-index: 1;
}
.speech-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #222;
}
.speech-sub {
    margin-top: 10px;
    font-size: 1.1rem;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

# 대사 설정 함수
def get_speech():
    step = st.session_state.step
    if step == 0 and not st.session_state.industry_confirmed:
        return "“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”", "어떤 분야에서 승부할지, 네 선택을 보여줘."
    elif step == 0 and st.session_state.industry_confirmed:
        return f"“{st.session_state.industry}... 흥미로운 선택이군.”", f"✅ 이미 선택한 업종: {st.session_state.industry}"
    elif step == 1:
        return "“이제 회사를 설립할 시간이야.”", "멋진 회사 이름을 지어보자!"
    elif step == 2:
        return "“갑작스러운 상황 발생!”", "상황에 맞는 전략을 선택하자."
    elif step == 3:
        return "“전략이 실행됐어.”", "성과를 정리해보자."
    else:
        return "", ""

# 배경 이미지 + 말풍선 출력
title_text, sub_text = get_speech()
st.markdown(f"""
<div class="container">
    <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png" />
    <div class="speech-bubble">
        <div class="speech-title">{title_text}</div>
        <div class="speech-sub">{sub_text}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 단계별 UI 흐름
step = st.session_state.step

if step == 0:
    st.markdown("### Step 1: 업종 선택")
    if not st.session_state.industry_confirmed:
        industries = ["💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사", "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"]
        selected = st.selectbox("회사 업종을 선택해주세요", industries)
        if st.button("업종 확정"):
            st.session_state.industry = selected
            st.session_state.industry_confirmed = True
            st.rerun()
    else:
        if st.button("다음 ▶️"):
            st.session_state.step = 1

elif step == 1:
    st.markdown("### Step 2: 회사 이름 짓기")
    name_input = st.text_input("회사 이름을 입력하세요", max_chars=20)
    if st.button("회사 이름 확정"):
        if name_input.strip():
            st.session_state.company_name = name_input.strip()
            st.success("회사 이름이 등록되었습니다!")
        else:
            st.warning("회사 이름을 입력해주세요.")
    if st.session_state.company_name and st.button("다음 ▶️"):
        st.session_state.step = 2

elif step == 2:
    st.markdown("### Step 3: 위기/기회 상황 대응")

    situations = [
        ("⚠️ 대규모 고객 데이터 유출 발생", ["보안 시스템 전면 재구축", "PR 대응으로 신뢰 회복"]),
        ("📈 갑작스러운 수요 폭증", ["생산 라인 확장", "기술 투자로 대응"]),
        ("💸 원자재 가격 급등", ["공급처 다변화", "재고 최소화 전략"]),
        ("🔥 경쟁사의 파산", ["인재 채용 강화", "공격적 마케팅"]),
        ("📉 주요 제품 매출 급감", ["제품 리뉴얼", "광고 캠페인"]),
        ("🏆 대기업으로부터 투자 제안", ["지분 일부 매각", "독자 성장 고수"]),
        ("🌍 글로벌 시장 진출 기회", ["글로벌 파트너십 체결", "현지화 전략"])
    ]

    situation, options = random.choice(situations)
    st.session_state.situation = situation
    st.markdown(f"#### 상황: {situation}")
    strategy = st.radio("당신의 대응 전략은?", options)

    if st.button("전략 확정"):
        st.session_state.strategy = strategy
        # 점수 계산
        if strategy == effective_strategies.get(situation):
            st.session_state.score += 10
        else:
            st.session_state.score += 5
        st.session_state.history.append((situation, strategy))
        st.session_state.step = 3

elif step == 3:
    st.markdown("### 🏁 최종 경영 평가")
    st.write(f"**'{st.session_state.company_name}'은 다음과 같은 상황에 직면했습니다:**")
    st.write(f"📌 **{st.session_state.situation}**")
    st.write(f"👉 이에 대한 전략은: **{st.session_state.strategy}**")
    st.write(f"🏆 최종 점수: **{st.session_state.score}점**")

    if st.button("🔁 처음부터 다시 시작"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
