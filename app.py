import streamlit as st
from chat import *
import os
os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

st.set_page_config(
        page_title="師大附中小助手",
        page_icon="school",
        layout="wide",
    )
#圖片
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq0_NPKm8RiU5exq59qsYZoqLTfgpzmghjig&s",width=100)
st.header("師大附中小助手", divider='rainbow')
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("今晚，我想來點期末考日期與考程"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    
    response = f"你最棒的助手: {get_response(prompt)}"#把前面的prompt改成要輸出的東西
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})