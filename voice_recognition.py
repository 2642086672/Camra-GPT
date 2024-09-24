import speech_recognition as sr

def recognize_speech_google(audio):
    """使用 Google 语音识别服务将音频转换为文本"""
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio, language='zh-CN')  # 使用中文识别
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        raise Exception("无法连接到语音识别服务。")
