import streamlit as st

menu = st.sidebar.selectbox("성적 채점 서비스", ['로그인', '회원가입','마이페이지', '모의고사 채점', '내신 채점'])

if menu == '로그인':
    st.title("로그인")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("로그인")

elif menu == "회원가입":
    st.subheader("회원가입")
    id_input = st.text_input("ID")
    pw_input = st.text_input("pw", type="password")
    user_type = st.radio("회원 타입", ["학생", "학부모"])
    grade = st.selectbox("학생(자녀) 학년", ["중1", "중2", "중3", "고1", "고2", "고3", "N수"])
    if st.button("회원가입"):
        st.success(" 회원가입이 완료되었습니다!")

elif menu == '모의고사 채점' :
    st.subheader("모의고사 채점")

    test = st.selectbox("구분", [
        "2021 고3 3월 모의고사", "2021 고3 6월 모의고사", "2021 고3 9월 모의고사",
        "2022 고3 3월 모의고사", "2022 고3 6월 모의고사", "2022 고3 9월 모의고사",
        "2023 고3 3월 모의고사", "2023 고3 6월 모의고사", "2023 고3 9월 모의고사",
        "2024 고3 3월 모의고사", "2024 고3 6월 모의고사", "2024 고3 9월 모의고사"
    ])

    
    st.subheader("국어")
    koreanselect = st.radio("국어", ["언어와 매체", "화법과 작문"])
    korean1_5 = st.text_input("1번 ~ 5번")
    korean6_10 = st.text_input("6번 ~ 10번")
    korean11_15 = st.text_input("11번 ~ 15번")
    korean16_20 = st.text_input("16번 ~ 20번")
    korean21_25 = st.text_input("21번 ~ 25번")
    korean26_30 = st.text_input("26번 ~ 30번")
    korean31_35 = st.text_input("31번 ~ 35번")
    korean36_40 = st.text_input("36번 ~ 40번")
    korean41_45 = st.text_input("41번 ~ 45번")

    st.subheader("수학")
    mathselect = st.selectbox("수학 과목 선택", ["미적분", "기하", "확률과 통계"])

    st.subheader("객관식 문제")
    math1_5 = st.text_input("1번 ~ 5번", )
    math6_10 = st.text_input("6번 ~ 10번", )
    math11_15 = st.text_input("11번 ~ 15번", )

    st.subheader("주관식 문제")
    math16_22= st.text_input("16번 ~ 22번 주관식 답 입력")

    st.subheader("선택과목 문제")
    st.write("선택 과목:",  mathselect )
    math23_28 = st.text_input("23번 ~ 28번",)

    st.subheader("주관식 문제 (29~30번)")
    math29_30 = st.text_input("29번 ~ 30번 주관식 답 입력")

    if st.button("채점하기"):
        st.success("채점이 완료되었습니다")

elif menu == '마이페이지' :
    st.subheader("채점 결과")
