import pyttsx3

def text_to_speech(text):
    """将文本转换为语音并播放"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
