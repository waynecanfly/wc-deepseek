from flask import Flask, request, abort
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from dotenv import load_dotenv
import os
from deepseek_client import DeepSeekClient

# 加载环境变量
load_dotenv()

# 初始化DeepSeek客户端
deepseek_client = DeepSeekClient()

# 获取环境变量
TOKEN = os.getenv('WECHAT_TOKEN')
AES_KEY = os.getenv('WECHAT_AES_KEY')
APP_ID = os.getenv('WECHAT_APP_ID')

app = Flask(__name__)

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    # 微信服务器验证请求
    if request.method == 'GET':
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
            return echostr
        except InvalidSignatureException:
            abort(403)
    
    # 处理微信消息
    if request.method == 'POST':
        try:
            msg = parse_message(request.data)
            if msg.type == 'text':
                # 调用DeepSeek API处理用户消息
                response = deepseek_client.chat(msg.content)
                reply = create_reply(response, msg)
                return reply.render()
            else:
                reply = create_reply('目前只支持文本消息', msg)
                return reply.render()
        except Exception as e:
            print(f'Error: {str(e)}')
            abort(500)

if __name__ == '__main__':
    app.run(debug=True)