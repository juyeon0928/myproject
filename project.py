import streamlit as st
import sqlite3



st.set_page_config(
    page_title="성적 채점 서비스",
    page_icon="📃"  
)


conn = sqlite3.connect('dbproject.db')
cursor = conn.cursor()
menu = st.sidebar.selectbox("메뉴 선택", ['로그인', '회원가입', '마이페이지', '모의고사 채점', '내신 채점'])

if menu == '로그인':
    st.title("로그인")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("로그인")
    if btn:
        cursor.execute(f"SELECT username, pw FROM user WHERE username='{id}'")
        row = cursor.fetchone()

        if row:
            db_id = row[0]
            db_pw = row[1]
            
            if db_pw == pw:
                st.sidebar.write(f"{db_id}님 환영합니다.")
            else:
                st.error("로그인 실패! 비밀번호가 일치하지 않습니다.")
        else:
            st.error("로그인 실패! 아이디가 존재하지 않습니다.")

        

elif menu == "회원가입":
    conn = sqlite3.connect('dbproject.db')
    cursor = conn.cursor()
    st.subheader("회원가입")
    id = st.text_input("ID")
    pw = st.text_input("비밀번호", type="password")
    pw_check = st.text_input("비밀번호 확인", type='password')
    usertype = st.radio("회원 타입", ["학생", "학부모"])
    grade = st.selectbox("학생(자녀) 학년", ["중1", "중2", "중3", "고1", "고2", "고3", "N수"])
    
    
    if st.button("회원가입"):
        
        if pw == pw_check:            
            
            sql = f"""
insert into user(username, pw, usertype, grade)
values('{id}','{pw}','{usertype}','{grade}')"""
            cursor.execute(sql)
            conn.commit()
            conn.close()
            st.success("회원가입 성공!")
        else:
            st.error("비밀번호가 일치하지 않습니다.")
    

elif menu == '모의고사 채점':
    st.subheader("모의고사 채점")

    test = st.selectbox("구분", [
        "2021 고3 3월 모의고사", "2021 고3 6월 모의고사", "2021 고3 9월 모의고사",
        "2022 고3 3월 모의고사", "2022 고3 6월 모의고사", "2022 고3 9월 모의고사",
        "2023 고3 3월 모의고사", "2023 고3 6월 모의고사", "2023 고3 9월 모의고사",
        "2024 고3 3월 모의고사", "2024 고3 6월 모의고사", "2024 고3 9월 모의고사"
    ])

    st.subheader("국어")
    correct_answer = {
        "2021 고3 3월 모의고사": {
            "answer": "1325155354151241122323423145444512",
            "threepoint": [3, 8, 15, 18, 25, 28, 32],
            "korean": {
                "언어와 매체": {
                    "answer": "22331354435",
                    "threepoint": [35, 41]
                },
                "화법과 작문": {
                    "answer": "53541433232",
                    "threepoint": [37, 43]
                }
            }
        }
    }
    koreanselect = st.radio("국어", ["언어와 매체", "화법과 작문"])
    c1, c2=st.columns(2)
    korean1_5 = c1.text_input("1번 ~ 5번", key="korean1_5")
    korean6_10 = c2.text_input("6번 ~ 10번", key="korean6_10")
    korean11_15 = c1.text_input("11번 ~ 15번", key="korean11_15")
    korean16_20 = c2.text_input("16번 ~ 20번", key="korean16_20")
    korean21_25 = c1.text_input("21번 ~ 25번", key="korean21_25")
    korean26_30 = c2.text_input("26번 ~ 30번", key="korean26_30")
    korean31_35 = c1.text_input("31번 ~ 35번", key="korean31_35")
    korean36_40 = c2.text_input("36번 ~ 40번", key="korean36_40")
    korean41_45 = c1.text_input("41번 ~ 45번", key="korean41_45")

    if st.button("국어 채점하기"):
        score = 0
        correct_count = []

        user_answer = [
        korean1_5, korean6_10, korean11_15, korean16_20, korean21_25,
        korean26_30, korean31_35, korean36_40, korean41_45
    ]
        user_answer = [answer for group in user_answer for answer in group]


        for i in range(34):
            if user_answer[i] == correct_answer[test]["answer"][i]:
                score += 3 if (i + 1) in correct_answer[test]["threepoint"] else 2
            else:
                correct_count.append(i + 1)

        
        korean_answers = correct_answer[test]["korean"][koreanselect]["answer"]
        korean_threepoint = correct_answer[test]["korean"][koreanselect]["threepoint"]

        for i in range(len(korean_answers)):
            user_answer_i = user_answer[i + 34]  
            if user_answer_i == korean_answers[i]:
                score += 3 if (i + 35) in korean_threepoint else 2
            else:
                correct_count.append(i + 35)

        st.success(f"총 점수: {score}점")
        if correct_count:
            st.write(':red[틀린 문제 번호:]', ', '.join(map(str, correct_count)) if correct_count else "만점🎇")




    st.subheader("수학")
    mathselect = st.selectbox("수학 과목 선택", ["미적분", "기하", "확률과 통계"])

    st.subheader("객관식 문제")
    math1_5 = st.text_input("1번 ~ 5번", key="math1_5")
    math6_10 = st.text_input("6번 ~ 10번", key="math6_10")
    math11_15 = st.text_input("11번 ~ 15번", key="math11_15")

    st.subheader("주관식 문제")
    math16_22 = st.text_input("16번 ~ 22번 주관식 답 입력", key="math16_22")

    st.subheader("선택과목 문제")
    st.write("선택 과목:", mathselect)
    math23_28 = st.text_input("23번 ~ 28번", key="math23_28")

    st.subheader("주관식 문제 (29~30번)")
    math29_30 = st.text_input("29번 ~ 30번 주관식 답 입력", key="math29_30")

    if st.button("수학 채점하기"):
        st.success("채점이 완료되었습니다")

elif menu == '마이페이지':
    st.subheader("채점 결과")

conn.close()
