from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(api_key='这里写你的Api')

# 用于保存对话上下文
conversation_history = []

def analyze_image_with_gpt4_o(image_base64):
    """使用 GPT-4o 进行图像分析，并保持对话上下文"""
    global conversation_history

    # 添加当前图像请求到对话历史
    conversation_history.append({
        "role": "user",
        "content": [
            {"type": "text", "text": "请描述这张图像的内容："},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
    })

    # 调用 GPT-4o API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        max_tokens=300
    )

    # 提取模型回应并更新对话历史
    model_response = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": model_response
    })

    # Debugging: Print the raw response
    print("Raw response:", response)

    return model_response

def analyze_text_with_gpt4_o(text):
    """使用 GPT-4o 处理文本，并保持对话上下文"""
    global conversation_history

    # 添加当前文本请求到对话历史
    conversation_history.append({
        "role": "user",
        "content": text
    })

    # 调用 GPT-4o API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        max_tokens=300
    )

    # 提取模型回应并更新对话历史
    model_response = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": model_response
    })

    # Debugging: Print the raw response
    print("Raw response:", response)

    return model_response