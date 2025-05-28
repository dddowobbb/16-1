import streamlit as st

# 초기 단계 설정
if "step" not in st.session_state:
    st.session_state.step = 0

# 회사 이름 저장 변수 초기화
if "company_name" not in st.session_state:
    st.session_state.company_name = ""

st.title("📈 경영 시뮬레이터: 나만의 회사를 만들어보자!")

# Step 0: 회사 이름 입력
if st.session_state.step == 0:
    st.subheader("Step 1: 회사 이름을 지어주세요 🏢")
    company_input = st.text_input("원하는 회사 이름을 입력하세요", max_chars=20)

    if st.button("확정"):
        if company_input.strip() == "":
            st.warning("회사 이름을 입력해주세요!")
        else:
            st.session_state.company_name = company_input.strip()
            st.session_state.step = 1
            st.success(f"'{st.session_state.company_name}'이(가) 성공적으로 등록되었습니다!")

# Step 1: 다음 단계로 이동
elif st.session_state.step == 1:
    st.subheader(f"'{st.session_state.company_name}'의 CEO가 되어 경영을 시작합니다!")
    st.write("이제 본격적으로 전략을 선택하고 회사를 성장시켜 보세요.")
    if st.button("다음으로 ▶️"):
        st.session_state.step = 2  # 다음 단계로 이동

# 이후 단계는 별도 구현 가능 (예: 전략 선택, 위기 상황 등)
