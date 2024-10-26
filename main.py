import streamlit as st

st.write("test")
st.header('제목')
st.subheader('1. 공동교육과정')
st.divider()
st.markdown(":red[**공동**]교육과정")
button=st.button('버튼')
if button:
    st.write("버튼 클릭!!")

a=st.number_input("1번 숫자를 입력하세요", step=1)
b=st.number_input("2번 숫자를 입력하세요", step=1)
btn=st.button("더하기")
if btn:
    st.write(a+b)
btn2=st.button("빼기")
if btn2:
    st.write(a-b)
btn3=st.button("곱하기")
if btn3:
    st.write(a*b)
btn4=st.button("나누기")
if btn4:
    st.write(a/b)