import streamlit as st
from openai import OpenAI

# Streamlit Cloud에서도 작동하도록 secrets 사용
api_key = st.secrets.get("OPENAI_API_KEY", None)
if not api_key:
    st.error("API 키가 설정되지 않았습니다. Streamlit Secrets에 등록해주세요.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("나만의 GPT 앱 💬")
user_input = st.text_area("질문을 입력하세요:")

if st.button("답변 받기") and user_input:
    with st.spinner("GPT가 답변 중..."):
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7
        )
        st.success(res.choices[0].message.content)

