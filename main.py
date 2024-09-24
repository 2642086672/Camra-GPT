import cv2
import pyttsx3
import base64
import threading
from voice_recognition import recognize_speech_google
from gpt_analysis import analyze_image_with_gpt4_o, analyze_text_with_gpt4_o
import speech_recognition as sr

# 初始化语音识别和合成
engine = pyttsx3.init()
listening = True

def adjust_exposure(cap):
    """调整摄像头的曝光设置"""
    exposure_value = -4  # 初始曝光值
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure_value)  # 设置初始曝光值
    print(f"初始曝光值: {exposure_value}")

    for _ in range(10):  # 尝试不同的曝光值
        cap.set(cv2.CAP_PROP_EXPOSURE, exposure_value)
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Exposure Adjustment", frame)
            print(f"当前曝光值: {exposure_value}")
            key = cv2.waitKey(1000)  # 等待 1 秒
            if key == 27:  # 按 'ESC' 键退出调整
                break
        exposure_value += 1  # 增加曝光值

    cv2.destroyAllWindows()  # 关闭图像窗口

def increase_brightness(image_path, beta=50):
    """增加图像亮度"""
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图像")
        return None

    # 增加亮度
    bright_image = cv2.convertScaleAbs(image, alpha=1, beta=beta)
    
    # 保存亮度调整后的图像
    bright_image_path = image_path.replace('.jpeg', '_bright.jpeg')
    cv2.imwrite(bright_image_path, bright_image)
    print(f"亮度调整后的图像已保存为 {bright_image_path}")

    return bright_image_path

def capture_image_from_camera():
    """从摄像头捕捉图像并保存为文件"""
    try:
        cap = cv2.VideoCapture(0)  # 打开默认摄像头
        if not cap.isOpened():
            print("无法打开摄像头")
            return None

        # 尝试自动调整曝光
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)  # 启用自动曝光

        print("请对着摄像头...")
        ret, frame = cap.read()  # 捕捉一帧
        cap.release()  # 释放摄像头

        if ret:
            image_path = '/Users/meikailong/Downloads/A.jpeg'  # 更新为所需的图像保存路径
            cv2.imwrite(image_path, frame)  # 保存图像

            # 调整图像亮度
            bright_image_path = increase_brightness(image_path)
            print(f"图像已保存为 {bright_image_path}")
            return bright_image_path
        else:
            print("无法捕捉图像")
            return None

    except cv2.error as e:
        print(f"OpenCV 错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

def image_to_base64(image_path):
    """将图像转换为 base64 编码"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def listen_for_commands():
    global listening
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000  # 调整灵敏度

    with sr.Microphone() as source:
        while listening:
            try:
                print("正在监听...")
                audio = recognizer.listen(source, timeout=5)
                text = recognize_speech_google(audio)
                print(f"你说的是: {text}")

                if "识别" in text:
                    print("开始捕捉图像...")
                    image_path = capture_image_from_camera()
                    if image_path:
                        image_base64 = image_to_base64(image_path)
                        result = analyze_image_with_gpt4_o(image_base64)
                        print(f"GPT-4 Vision 的回应：{result}")  # 确保结果被打印到终端
                        engine.say(f"GPT-4 Vision 的回应：{result}")
                        engine.runAndWait()

                elif "结束录音" in text:
                    print("检测到 '结束录音'，录音结束。")
                    listening = False

                elif text:
                    # 处理其他文本指令
                    response = analyze_text_with_gpt4_o(text)
                    print(f"GPT-4 的回应：{response}")
                    engine.say(f"GPT-4 的回应：{response}")
                    engine.runAndWait()

            except sr.UnknownValueError:
                print("对不起，我无法理解你说的话。")
            except sr.RequestError:
                print("对不起，无法连接到语音识别服务。")
            except Exception as e:
                print(f"发生错误: {e}")

def background_gpt_conversation():
    """后台线程函数，用于与 GPT-4 对话"""
    global listening
    while listening:
        # 检测到人声时，启动对话逻辑
        pass  # 在这里添加与 GPT-4 的对话逻辑

def main():
    global listening
    print("程序启动。请说出 '识别' 来开始图像识别。")

    # 启动监听线程
    listen_thread = threading.Thread(target=listen_for_commands)
    listen_thread.start()

    # 启动后台对话线程
    gpt_thread = threading.Thread(target=background_gpt_conversation)
    gpt_thread.start()

    listen_thread.join()
    gpt_thread.join()

if __name__ == "__main__":
    main()
