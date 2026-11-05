import streamlit as st
import time
audio_file_name = "mysong.mp3"
st.container(border=True).write("<center><h2> saad dine </h2></center>",unsafe_allow_html=True)
try:
    with open(audio_file_name, "rb") as f:
        audio_bytes = f.read()
        st.audio(audio_bytes, format="audio.mp3", loop=True, autoplay=True)
        st.video("myvideo.mp4", loop=True, autoplay=True, muted=True,)
except FileNotFoundError:
    pass
name = st.text_input(":ادخل اسمك")
age = st.number_input(":ادخل عمرك",min_value=1, step=1)
if st.button("تأكيد"):
    if name:
        st.info(f" 🌟مرحبا بك يا{name} 🌟", icon="🌟")
        st.success(f"مرحبا{name}!تم الحساب بنجاح .")
        st.balloons()
        time.sleep(30)
