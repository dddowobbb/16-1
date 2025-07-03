import streamlit as st

st.set_page_config(layout="wide")

# 세션 상태 초기화
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False

# 💡 배경 이미지 + 말풍선 스타일
st.markdown("""
<style>
    .stApp {
        background: url("https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .speech-box {
        position: relative;
        top: 65vh;  /* 얼굴 밑으로 내려서 겹치게 */
        margin: 0 auto;
        width: 60%;
        background: rgba(255, 255, 255, 0.85);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        z-index: 2;
        text-align: center;
    }

    .speech-text {
        font-size: 20px;
        font-weight: bold;
        color: #222;
        margin-bottom: 0.5rem;
    }

    .speech-sub {
        font-size: 16px;
        color: #555;
        margin-bottom: 1rem;
    }

    .block-container {
        padding-top: 0rem;
    }
</style>
""", unsafe_allow_html=True)

# 🗣️ 말풍선 안의 텍스트 및 선택 UI
st.markdown("<div class='speech-box'>", unsafe_allow_html=True)

# CEO 말풍선 멘트
if not st.session_state.industry_confirmed:
    st.markdown("<div class='speech-text'>“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”</div>", unsafe_allow_html=True)
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
        st.success(f"✅ 선택된 업종: {selected}")
else:
    st.markdown(f"<div class='speech-text'>“{st.session_state.industry}... 흥미로운 선택이군.”</div>", unsafe_allow_html=True)
    st.success(f"✅ 이미 선택한 업종: {st.session_state.industry}")

st.markdown("</div>", unsafe_allow_html=True)
