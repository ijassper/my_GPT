import os
from openai import OpenAI
from dotenv import load_dotenv

# 환경 변수에서 키 불러오기 (.env에 OPENAI_API_KEY 저장된 경우)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API 키가 없습니다. .env 파일 또는 환경변수를 확인하세요.")
    exit()

try:
    client = OpenAI(api_key=api_key)
    models = client.models.list()  # 모델 목록 요청
    print("✅ API 키가 유효합니다!")
    print("사용 가능한 모델 예시:", [model.id for model in models.data[:3]])
except Exception as e:
    print("❌ API 키가 유효하지 않거나 인증에 실패했습니다.")
    print("에러 메시지:", e)
