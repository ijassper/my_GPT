import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="My GPT App", page_icon="🤖", layout="centered")

# OpenAI 클라이언트 설정
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 세션 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- 상단: 대화 영역 ----
st.title("🧠 나만의 GPT")

chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ---- 하단: 입력 박스 고정 ----
# 빈 공간으로 밀어내기
st.markdown("---")
st.markdown("### 💬 질문을 입력하세요")

# 하단 입력 영역
with st.container():
    user_input = st.chat_input("여기에 질문을 입력하세요...")

# 사용자 입력 처리
if user_input:
    # 사용자 메시지 저장 및 출력
    st.session_state.messages.append({"role": "user", "content": user_input})
    with chat_container:
        with st.chat_message("user"):
            st.markdown(user_input)

    # GPT 응답 처리
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )

        for chunk in response:
            chunk_message = chunk.choices[0].delta.content or ""
            full_response += chunk_message
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # GPT 메시지 저장
    st.session_state.messages.append({"role": "assistant", "content": full_response})
