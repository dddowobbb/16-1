import streamlit as st

# 전체 화면 설정
st.set_page_config(layout="wide")

# 세션 상태 초기화
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False

# ✅ CSS 스타일링
st.markdown("""
    <style>
        .container {
            position: relative;
            width: 100%;
            height: 90vh;
            overflow: hidden;
        }
        .bg-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .speech-bubble {
            position: absolute;
            top: 68vh;
            left: 50%;
            transform: translateX(-50%);
            width: 75%;
            background: rgba(255, 255, 255, 0.85);
            padding: 25px 30px;
            border-radius: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            text-align: center;
        }
        .speech-title {
            font-size: 1.5rem;
            font-weight: bold;
            color: #222;
        }
        .speech-sub {
            margin-top: 8px;
            font-size: 1.1rem;
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ CEO 이미지와 말풍선 텍스트 출력 (업종 선택 여부에 따라 다르게 표시)
st.markdown("""
<div class="container">
    <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png" />
    <div class="speech-bubble">
""", unsafe_allow_html=True)

if not st.session_state.industry_confirmed:
    # 선택 전 멘트
    st.markdown("""
        <div class="speech-title">“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”</div>
        <div class="speech-sub">어떤 분야에서 승부할지, 네 선택을 보여줘.</div>
    """, unsafe_allow_html=True)
else:
    # 선택 후 멘트
    st.markdown(f"""
        <div class="speech-title">“{st.session_state.industry}... 흥미로운 선택이군.”</div>
        <div class="speech-sub">✅ 이미 선택한 업종: {st.session_state.industry}</div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ✅ 업종 선택 UI
st.markdown("### Step 1: 업종을 선택하세요 🔍")

industries = [
    "💻 IT 스타트업",
    "🌱 친환경 제품",
    "🎮 게임 개발사",
    "👗 패션 브랜드",
    "🍔 푸드테크",
    "🛒 글로벌 전자상거래"
]

if not st.session_state.industry_confirmed:
    selected = st.selectbox("회사 업종을 선택해주세요", industries)
    if st.button("업종 확정"):
        st.session_state.industry = selected
        st.session_state.industry_confirmed = True
        st.rerun()
else:
    st.info(f"✅ 이미 선택한 업종: {st.session_state.industry}")
