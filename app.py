import streamlit as st

st.set_page_config(layout="wide")

# 세션 상태 초기화
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False

# 💡 전체 화면 배경 이미지 + 말풍선 스타일
st.markdown("""
<style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .speech-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        width: 70%;
        margin: 70vh auto 0 auto;  /* ⬅ 인물 아래 위치 */
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }

    select, button {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# 💬 말풍선 안에 업종 선택 UI
with st.container():
    st.markdown("<div class='speech-box'>", unsafe_allow_html=True)

    st.markdown("### Step 1: 업종을 선택하세요 🔍")

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
            st.success(f"✅ 선택된 업종: {selected}")
    else:
        st.success(f"✅ 이미 선택한 업종: {st.session_state.industry}")

    st.markdown("</div>", unsafe_allow_html=True)
