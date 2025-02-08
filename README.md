# 🤖 微信公众号 DeepSeek AI 助手

一个基于 DeepSeek API 的智能对话机器人，可以轻松地将 AI 对话能力集成到您的微信公众号中。

## ✨ 主要特点

- 🔌 快速集成：只需简单配置即可将 DeepSeek AI 接入您的微信公众号
- 🤝 智能对话：支持自然语言交互，为用户提供智能对话服务
- ⚡ 实时响应：快速处理用户消息，提供即时的 AI 回复
- 🛡️ 异常处理：完善的错误处理机制，确保服务稳定运行
- 🔒 安全可靠：支持微信服务器安全验证，保护您的服务

## 🚀 快速开始

### 环境要求

- Python 3.7+
- 微信公众号账号
- DeepSeek API 密钥

### 安装步骤

1. 克隆项目代码：
```bash
git clone [您的项目地址]
cd wc-deepseek
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
   - 复制 `.env.example` 文件为 `.env`
   - 填入您的配置信息：
```env
# 微信公众号配置
WECHAT_TOKEN=your_token_here
WECHAT_AES_KEY=your_aes_key_here
WECHAT_APP_ID=your_app_id_here

# DeepSeek API配置
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_API_ENDPOINT=https://api.deepseek.com/v1
```

4. 启动服务：
```bash
python app.py
```

## 📝 配置说明

### 微信公众号配置
1. 登录微信公众平台
2. 进入「基本配置」页面
3. 获取 AppID 和 AES Key
4. 设置服务器配置：
   - URL：设置为您的服务器地址 + `/wechat`
   - Token：与 `.env` 中的 `WECHAT_TOKEN` 保持一致
   - EncodingAESKey：与 `.env` 中的 `WECHAT_AES_KEY` 保持一致

### DeepSeek API 配置
1. 注册 DeepSeek 开发者账号
2. 获取 API Key
3. 将 API Key 填入 `.env` 文件的 `DEEPSEEK_API_KEY` 字段

## 💡 使用示例

1. 确保服务正常运行
2. 关注配置好的微信公众号
3. 向公众号发送文本消息
4. 等待 AI 助手的智能回复

## 🔧 自定义配置

您可以通过修改 `deepseek_client.py` 中的参数来自定义 AI 对话的行为：

```python
data = {
    'model': 'deepseek-chat',  # AI 模型
    'temperature': 0.7,         # 回复的创造性程度
    'max_tokens': 1000          # 最大回复长度
}
```
