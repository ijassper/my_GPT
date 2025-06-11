import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("나만의 GPT 앱 💬")

user_input = st.text_area("질문을 입력하세요:")

if st.button("답변 받기"):
    if user_input:
        with st.spinner("GPT가 답변 중..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # 또는 "gpt-4"
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,
            )
            answer = response['choices'][0]['message']['content']
            st.success(answer)
    else:
        st.warning("먼저 질문을 입력해주세요.")
