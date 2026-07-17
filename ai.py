import os
import requests
from dotenv import load_dotenv

load_dotenv()


def analyze_profile(data):

    api_key = os.getenv("DEEPSEEK_API_KEY")

    prompt = f"""
You are an admission advisor.

Analyze this student's university profile.

GPA: {data["gpa"]}
IELTS: {data["ielts"]}
SAT: {data["sat"]}

Portfolio:
{data["portfolio"]}

Target universities:
{data["universities"]}

Give:
1. Admission chances
2. Strengths
3. Weaknesses
4. Recommendations
"""

    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]