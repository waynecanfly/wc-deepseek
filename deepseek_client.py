import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class DeepSeekClient:
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.api_endpoint = os.getenv('DEEPSEEK_API_ENDPOINT')
        if not self.api_key or not self.api_endpoint:
            raise ValueError('DeepSeek API配置缺失')

    def chat(self, message):
        """发送消息到DeepSeek API并获取回复"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            'messages': [
                {'role': 'user', 'content': message}
            ],
            'model': 'deepseek-chat',
            'temperature': 0.7,
            'max_tokens': 1000
        }

        try:
            response = requests.post(
                f'{self.api_endpoint}/chat/completions',
                headers=headers,
                json=data
            )
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            print(f'DeepSeek API请求失败: {str(e)}')
            return '抱歉，我现在无法回答，请稍后再试。'