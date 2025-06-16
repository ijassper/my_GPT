# app.py
import streamlit as st
from openai import OpenAI
import os

# API 키 불러오기
api_key = st.secrets.get("OPENAI_API_KEY", "")  # 또는 os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API 키가 설정되지 않았습니다.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("나만의 GPT 앱 ✨")
user_input = st.text_area("무엇이든 물어보세요:")

if st.button("응답 받기") and user_input:
    with st.spinner("GPT 응답 생성 중..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7
            )
            st.success("답변:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"에러 발생: {e}")
