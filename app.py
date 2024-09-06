import streamlit as st
import time
import pandas as pd

st.title("Welcome to My Website")

st.header("This is my header")
st.subheader("this is my sub header")
data=st.file_uploader(label="data for the simple upload test",type="txt")
if data is not None:
    # To read file as bytes:
    bytes_data = data.getvalue()
    st.write(bytes_data)


st.markdown("""
            This is Markeddown
            - satish
            - hiremath
            - adding "-" increates the list/. in UI
            """)
st.link_button(label="mark down guide",url="https://www.markdownguide.org/basic-syntax/")

st.link_button(label="LaTex in 30 min",url="https://www.overleaf.com/learn")

st.code("""
def foo(num):
    returnnum*2  
foo(3)
""")

st.latex('x^2+y^2=3')

datas=pd.DataFrame({'name':[1,2,3],'age':[12,13,14]})
st.dataframe(datas)

st.metric(label='revenue',value=100,delta=5)


st.json({'name':[1,2,3],'age':[12,13,14]})
#st.image
#st.video
#st.audio

st.sidebar.markdown("""
            This is Markeddown and just by adding sidebar all will become side
            - satish
            - hiremath
            - adding "-" increates the list/. in UI
            """)
col1,col2=st.columns(2)

with col1:
    st.write("this is columns")
with col2:
    st.write("this is in column2")

st.info("This is info msg")
st.error("This is error msg")
st.success("This is succuss msg")
st.warning("this warning msg")


bar=st.progress(0)

st.text_input(label="Enter email")
st.date_input(label="Enter the date")
st.number_input(label="enter phone number")
st.camera_input(label='camera')

button=st.button("Click for sidebar and bollon")
stop=st.button("click to stop ballon and sidebar")

while button:
    st.sidebar.balloons()
    time.sleep(5)
    for i in range(50):
        bar.progress(i)
        time.sleep(0.2)
    if stop:
        break


st.selectbox(label="gender",options=["male","female"])