# DeepSeek
import requests

# 这里填老师给的API Key和Bot ID
API_KEY = "你的API_KEY"
BOT_ID = "你的BOT_ID"

def chat(message):
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "bot_id": BOT_ID,
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]

# 测试运行
if __name__ == "__main__":
    question = "什么是数智化内部审计？"
    answer = chat(question)
    print("用户：", question)
    print("DeepSeek：", answer)