import streamlit as st

def 자기소개():
    st.header("자기소개 페이지")
def 학교소개():
    st.header("학교소개 페이지")
def 로그인():
    st.header('로그인')
    c1, c2=st.columns(2)
    id= c1.text_input("아이디",placeholder='아이디를 입력하세요.')
    pw= c2.text_input("비밀번호", placeholder="비밀번호를 입력하세요.", type="password")
def 김주연테스트():
    st.header('나에 관한 퀴즈를 맞춰보아요😍❤')
    st.image('image.png')
    a=st.number_input("**얼만큼 좋아하나요??**", step=1)
    if a>10000000000000:
            st.write(":blue[올 ㅋㅋ 정답]")
    else :
            st.write(":red[그정도밖에? ㅉㅉ]")

        
btn=st.button("로그인")
if btn:
    if id =='godkimchi999' and pw=='rlawndus123@':
        st.write("로그인 성공")
    else:
        st.write("로그인 실패")

st.sidebar.header("김주연의 홈페이지입니다.")
menu=st.sidebar.selectbox('Menu', ['로그인','자기소개', '학교소개', '김주연테스트'])

if menu == '자기소개':
    자기소개()
elif menu =="학교소개":
    학교소개()
elif menu =='로그인':
    로그인()
elif menu=='김주연테스트':
    김주연테스트()