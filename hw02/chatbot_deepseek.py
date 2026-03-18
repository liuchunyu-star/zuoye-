import requests

# 1. 这里必须填老师给你的真实 API Key 和 Bot ID
API_KEY = "sk-bee584fc43b54291800be39e6166089b"
BOT_ID = "https://api.deepseek.com"

def chat(message):
    """
    调用DeepSeek官方对话接口
    """
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "bot_id": BOT_ID,
        "messages": [{"role": "user", "content": message}]
    }
    
    try:
        response = requests.post(url, json=data)
        result = response.json()
        # 正确返回路径是 result["choices"][0]["message"]["content"]
        return result["choices"][0]["message"]["content"]
    except KeyError:
        return "报错：检查 API_KEY 或 BOT_ID 是否正确，或者网络是否连接。"

# 测试运行
if __name__ == "__main__":
    question = "内部审计"
    print(f"用户：{question}")
    print(f"DeepSeek回答：{chat(question)}")