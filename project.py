import streamlit as st
import sqlite3
from datetime import datetime

conn = sqlite3.connect('dbproject.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_results (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        test_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(id)
    );
''')

conn.commit()
conn.close()

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
                st.session_state.username = db_id
                st.sidebar.write(f"{db_id}님 환영합니다🎉")
                
            else:
                st.error("로그인 실패! 비밀번호가 일치하지 않습니다.")
        else:
            st.error("로그인 실패! 아이디가 존재하지 않습니다.")

elif menu == "회원가입":
    st.subheader("회원가입")
    id = st.text_input("ID")
    pw = st.text_input("비밀번호", type="password")
    pw_check = st.text_input("비밀번호 확인", type='password')
    usertype = st.radio("회원 타입", ["학생", "학부모"])
    grade = st.selectbox("학생(자녀) 학년", ["중1", "중2", "중3", "고1", "고2", "고3", "N수"])

    if st.button("회원가입"):
        if pw == pw_check:            
            sql = f"""
            INSERT INTO user(username, pw, usertype, grade)
            VALUES('{id}', '{pw}', '{usertype}', '{grade}')
            """
            cursor.execute(sql)
            conn.commit()
            conn.close()
            st.success("회원가입 성공!")
        else:
            st.error("비밀번호가 일치하지 않습니다.")

elif menu == '모의고사 채점':
    st.subheader("모의고사 채점")
    test = st.selectbox("구분", [
        "2021 고3 3월 모의고사", "2021 고3 6월 모의고사", "2021 고3 9월 모의고사", "2021 대학수학능력시험",
        "2022 고3 3월 모의고사", "2022 고3 6월 모의고사", "2022 고3 9월 모의고사", "2022 대학수학능력시험",
        "2023 고3 3월 모의고사", "2023 고3 6월 모의고사", "2023 고3 9월 모의고사", "2023 대학수학능력시험",
        "2024 고3 3월 모의고사", "2024 고3 6월 모의고사", "2024 고3 9월 모의고사",  "2024 대학수학능력시험",
    ])
    
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
    
    with st.container():
        st.subheader("국어")
        koreanselect = st.radio("국어", ["언어와 매체", "화법과 작문"])
        c3, c4 = st.columns(2)
        korean1_5 = c3.text_input("1번 ~ 5번", key="korean1_5")
        korean6_10 = c4.text_input("6번 ~ 10번", key="korean6_10")
        korean11_15 = c3.text_input("11번 ~ 15번", key="korean11_15")
        korean16_20 = c4.text_input("16번 ~ 20번", key="korean16_20")
        korean21_25 = c3.text_input("21번 ~ 25번", key="korean21_25")
        korean26_30 = c4.text_input("26번 ~ 30번", key="korean26_30")
        korean31_35 = c3.text_input("31번 ~ 35번", key="korean31_35")
        korean36_40 = c4.text_input("36번 ~ 40번", key="korean36_40")
        korean41_45 = c3.text_input("41번 ~ 45번", key="korean41_45")

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

            username = st.session_state.get('username')
            if username:
                cursor.execute('''
                    INSERT INTO test_results (user_id, test_name, score, test_date) 
                    VALUES ((SELECT id FROM user WHERE username = ?), ?, ?, ?)
                ''', (username, test, score, datetime.now()))
                conn.commit()
                st.success("채점 결과가 저장되었습니다.")

elif menu == '마이페이지':
    st.subheader("채점 결과")

    if 'username' not in st.session_state:
        st.warning("로그인이 필요합니다.")
    
    else:
        username = st.session_state.username
        
        conn = sqlite3.connect('dbproject.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM user WHERE username=?", (username,))
        user_id_row = cursor.fetchone()
        
        if user_id_row:
            user_id = user_id_row[0]
            
            cursor.execute("SELECT test_name, score, test_date FROM test_results WHERE user_id=?", (user_id,))
            results = cursor.fetchall()

            if results:
                st.write("최근 채점 기록:")
                for result in results:
                    test_name, score, test_date = result

                    st.markdown(f"**<span style='color: red; font-size: 15px; font-style: italic;'>시험 이름: {test_name}</span>**", unsafe_allow_html=True)
                    st.markdown(f"**<span style='color: blue; font-size: 25px; font-weight: bold;'>점수: {score}</span>**", unsafe_allow_html=True)
                    st.markdown(f"<span style='font-size: 10px;'>시험일: {test_date}</span>", unsafe_allow_html=True)
                    st.markdown("---")  
            else:
                st.write("채점 기록이 없습니다.")
        else:
            st.error("사용자 정보를 찾을 수 없습니다.")

        conn.close()



    

