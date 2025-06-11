import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("나만의 GPT 앱 💬")

user_input = st.text_area("질문을 입력하세요:")

if st.button("답변 받기"):
    if user_input:
        with st.spinner("GPT가 답변 중..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,
            )
            st.success(response.choices[0].message.content)
    else:
        st.warning("먼저 질문을 입력해주세요.")
