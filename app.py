import streamlit as st

# 화면 꽉 차게 설정
st.set_page_config(layout="wide")

# 세션 상태 초기화
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False
if "industry" not in st.session_state:
    st.session_state.industry = ""

# CSS 정의
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

# 이미지와 말풍선 (위쪽 고정 영역)
st.markdown("""
<div class="container">
    <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png" />
    <div class="speech-bubble">
        <div class="speech-title">“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”</div>
        <div class="speech-sub">어떤 분야에서 승부할지, 네 선택을 보여줘.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 업종 선택 UI (아래쪽 콘텐츠)
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
        st.success(f"선택된 업종: {selected}")
else:
    st.info(f"✅ 이미 선택한 업종: {st.session_state.industry}")
