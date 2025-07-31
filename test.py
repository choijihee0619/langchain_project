from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # 환경 변수에서 API 키 로드
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Assistant로서 사용자 질문에 자연어로 답변하세요."},
        {"role": "user", "content": "테스트입니다."}
    ]
)
print(response.choices[0].message.content)
