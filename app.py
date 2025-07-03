import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

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

# ✅ 스타일 정의
st.markdown("""
<style>
.container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    margin-bottom: 20px;
}
.bg-image {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 0;
}
.speech-bubble {
    position: absolute;
    bottom: 8vh;
    left: 50%;
    transform: translateX(-50%);
    width: 75%;
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

# ✅ 대사 선택
def get_speech():
    step = st.session_state.step
    if step == 0 and not st.session_state.industry_confirmed:
        return "“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”", "어떤 분야에서 승부할지, 네 선택을 보여줘."
    elif step == 0 and st.session_state.industry_confirmed:
        return f"“{st.session_state.industry}... 흥미로운 선택이군.”", f"✅ 이미 선택한 업종: {st.session_state.industry}"
    elif step == 1:
        return "“이제 회사를 설립할 시간이야.”", "멋진 회사 이름을 지어보자!"
    elif step == 2:
        return "“경영 전략을 선택해야 할 때군.”", "회사의 색깔을 결정할 핵심 선택이야."
    elif step == 3:
        return "“전략이 실행됐어.”", "이제 세상에 우리가 어떤 회사인지 보여주자."
    elif step == 4:
        return "“예기치 못한 일이 벌어졌군...”", "좋든 나쁘든, 리더는 상황에 적응해야 해."
    elif step == 5:
        return "“분기별 실적이 나왔어!”", "그래프를 보고 흐름을 파악해보자."
    elif step == 6:
        return "“올 한 해 수고 많았어.”", "회사의 성과를 되돌아보자."
    else:
        return "", ""

# ✅ 배경 + 말풍선 출력
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

# ✅ 아래 실제 콘텐츠 흐름
step = st.session_state.step

if step == 0:
    st.markdown("### Step 1: 업종 선택")
    if not st.session_state.industry_confirmed:
        industries = [
            "💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사",
            "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"
        ]
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
    st.markdown("### Step 3: 전략 선택")
    strategy = st.radio("전략을 선택하세요", [
        "🔬 연구개발(R&D)에 투자하여 기술 선도",
        "📢 마케팅을 강화하여 브랜드 인지도 상승",
        "🏭 생산 효율화를 통해 원가 절감",
        "🌐 해외 시장 진출 확대"
    ])
    if st.button("전략 확정"):
        st.session_state.strategy = strategy
    if st.session_state.strategy and st.button("다음 ▶️"):
        st.session_state.step = 3

elif step == 3:
    st.markdown("### Step 4: 전략 결과")
    st.write(f"'{st.session_state.company_name}'은 **{st.session_state.strategy}** 전략을 실행했습니다.")
    if st.button("다음 ▶️"):
        st.session_state.step = 4

elif step == 4:
    st.markdown("### Step 5: 예기치 못한 사건 발생")
    all_events = {
        "💻 IT 스타트업": [("🌟 투자 유치 성공!", 1.3), ("💥 보안 사고", 0.7)],
        "🌱 친환경 제품": [("🌿 정부 보조금", 1.2), ("🚫 환경 비판", 0.75)],
        "🎮 게임 개발사": [("🔥 신작 대히트", 1.4), ("🐞 버그로 이탈", 0.6)],
        "👗 패션 브랜드": [("👠 인플루언서 콜라보", 1.2), ("📉 트렌드 실패", 0.75)],
        "🍔 푸드테크": [("🥗 비건 호평", 1.2), ("⚠️ 안정성 논란", 0.7)],
        "🛒 글로벌 전자상거래": [("🛍️ 쇼핑 대성공", 1.3), ("🚚 물류대란", 0.7)]
    }
    if not st.session_state.event:
        st.session_state.event = random.choice(all_events.get(st.session_state.industry, []))
    event_text, multiplier = st.session_state.event
    st.info(f"이벤트 발생: {event_text}")
    if st.button("다음 ▶️"):
        st.session_state.revenue = [
            int(100 * multiplier * random.uniform(0.9, 1.1)) for _ in range(4)
        ]
        st.session_state.step = 5

elif step == 5:
    st.markdown("### Step 6: 분기별 매출")
    quarters = ["1분기", "2분기", "3분기", "4분기"]
    fig, ax = plt.subplots()
    ax.plot(quarters, st.session_state.revenue, marker='o')
    ax.set_ylabel("매출 (억 원)")
    ax.set_title("분기별 매출 추이")
    st.pyplot(fig)
    if st.button("다음 ▶️"):
        st.session_state.step = 6

elif step == 6:
    st.markdown("### 🏁 최종 경영 평가")
    total = sum(st.session_state.revenue)
    st.write(f"**'{st.session_state.company_name}'의 연간 총 매출은 {total}억 원입니다.**")
    if total >= 450:
        st.success("🎉 훌륭한 성과입니다!")
    elif total >= 350:
        st.info("👍 안정적인 성과입니다.")
    else:
        st.warning("📉 전략 수정이 필요해 보입니다.")
    if st.button("🔁 처음부터 다시 시작"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
