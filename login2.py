import streamlit as st
import sqlite3


menu = st.sidebar.selectbox("MENU", ['로그인', '회원가입', '회원정보 수정', '회원 탈퇴'])

if menu == '로그인':
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    #로그인 화면 구현
    st.title("로그인")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("로그인")

    #로그인 버튼을 클릭
    if menu == '로그인':
        st.title("로그인")
        id = st.text_input("아이디")
        pw = st.text_input("비밀번호", type="password")
        btn = st.button("로그인")

    if btn:
        cursor.execute(f"SELECT * FROM user WHERE id='{id}'")
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

elif menu == '회원가입':
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    #회원가입 화면
    st.title("회원가입")
    #아이디
    id = st.text_input("아이디")
    #비밀번호
    pw = st.text_input("비밀번호", type='password')
    #비밀번호 확인
    pw_check = st.text_input("비밀번호 확인", type='password')
    #이메일
    email = st.text_input("이메일")
    #성별(라디오버튼)
    gender = st.radio("성별을 선택하세요", ['male','female'])
    #회원가입 버튼
    btn = st.button("회원가입")

    #버튼을 누르면
    if btn:
        #비밀번호가 잘 입력되었는지를 확인
        if pw == pw_check:            
            #입력한 정보를 DB에 저장
            sql = f"""
insert into user(username, password, email, gender)
values('{id}','{pw}','{email}','{gender}')"""
            cursor.execute(sql)
            conn.commit()
            st.success("회원가입 성공!")
        else:
            #회원가입 실패
            st.error("비밀번호가 일치하지 않습니다.")
    conn.close()
elif menu == '회원정보 수정':
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    #회원정보 수정 화면
    st.title("회원정보 수정")
    #아이디
    id = st.text_input("아이디")
    #비밀번호
    pw = st.text_input("비밀번호", type='password')    
    #이메일
    email = st.text_input("이메일")
    #성별(라디오버튼)
    gender = st.radio("성별을 선택하세요", ['male','female'])
    #회원가입 버튼
    btn = st.button("수정")

    if btn:
        #UPDATE user SET id = "test1", pw="1234" WHERE id="test"
        sql=f"""
UPDATE user SET 
password = "{pw}",
email = "{email}",
gender = "{gender}"
WHERE username = "{id}" 
"""
        cursor.execute(sql)
        conn.commit()
elif menu == '회원 탈퇴':
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    st.title("회원탈퇴")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("탈퇴")

    if btn:
        sql=f"""
DELETE FROM user WHERE username = "{id}"
"""
        conn.execute(sql)
        conn.commit()