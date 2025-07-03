import streamlit as st

# 전체화면 구성
st.set_page_config(layout="wide")

# CSS: 배경 이미지 + 말풍선 스타일
st.markdown("""
    <style>
        .container {
            position: relative;
            width: 100%;
            height: 100vh;
        }
        .bg-image {
            width: 100%;
            height: 100vh;
            object-fit: cover;
        }
        .speech-bubble {
            position: absolute;
            top: 68vh; /* 말풍선 위치 (아래로 더 내리고 싶으면 수치 증가) */
            left: 50%;
            transform: translateX(-50%);
            width: 70%;
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

# HTML: 배경 이미지 + 말풍선 + 텍스트
st.markdown("""
<div class="container">
    <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png" />
    <div class="speech-bubble">
        <div class="speech-title">“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”</div>
        <div class="speech-sub">어떤 분야에서 승부할지, 네 선택을 보여줘.</div>
    </div>
</div>
""", unsafe_allow_html=True)
