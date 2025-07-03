import streamlit as st

st.set_page_config(layout="wide")

# 세션 상태 초기화
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False

# 💬 스타일 정의 (배경 + 말풍선 레이아웃)
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png");
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        padding: 0;
    }

    .speech-wrapper {
        position: absolute;
        top: 68vh;  /* 💡 인물 얼굴 밑으로 정확히 배치 */
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
        text-align: center;
        z-index: 100;
    }

    .speech-title {
        font-size: 20px;
        font-weight: 700;
        color: #222;
        margin-bottom: 0.5rem;
    }

    .speech-sub {
        font-size: 15px;
        color: #555;
        margin-bottom: 1.5rem;
    }

    .block-container {
        padding-top: 0rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 💬 말풍선 안 내용
st.markdown("<div class='speech-wrapper'>", unsafe_allow_html=True)

if not st.session_state.industry_confirmed:
    st.markdown("<div class='speech-title'>“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”</div>", unsafe_allow_html=True)
    st.markdown("<div class='speech-sub'>어떤 분야에서 승부할지, 네 선택을 보여줘.</div>", unsafe_allow_html=True)

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
        st.rerun()
else:
    st.markdown(f"<div class='speech-title'>“{st.session_state.industry}... 흥미로운 선택이군.”</div>", unsafe_allow_html=True)
    st.success(f"✅ 이미 선택한 업종: {st.session_state.industry}")

st.markdown("</div>", unsafe_allow_html=True)
