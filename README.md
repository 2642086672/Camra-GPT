# Camra-GPT

Camra-GPT 是一个基于 GPT-4 Vision 的图像识别和语音互动系统。该项目旨在通过摄像头捕捉图像，并使用 GPT-4 Vision 进行图像分析，同时结合语音识别和合成技术，与用户进行自然语言对话。

## 功能
- **测试环境**: MacOS14，Apple Silicon M1
- **图像捕捉**: 从摄像头捕捉图像并自动调整曝光。
- **图像分析**: 使用 GPT-4 Vision 对捕捉的图像进行分析。
- **语音识别**: 识别用户的语音指令，并根据指令执行相应操作。
- **语音合成**: 将 GPT-4 的回应转换为语音，并进行语音播放。
- **动态曝光调整**: 自动调整摄像头曝光，以确保图像清晰。

## 安装

1. **克隆项目**

    ```bash
    git clone https://github.com/2642086672/Camra-GPT.git
    cd Camra-GPT
    ```

2. **创建虚拟环境**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. **安装依赖**

    ```bash
    pip install -r requirements.txt
    ```

## 使用

1. **配置 API 密钥**

    在 `gpt_analysis.py` 文件中配置 GPT-4 API 密钥。

    ```python
    OPENAI_API_KEY = 'your-api-key-here'
    ```

2. **运行程序**

    ```bash
    python main.py
    ```

3. **操作说明**

    - 程序启动后，请说出 “识别” 来开始图像识别。
    - 程序将自动捕捉图像、调整曝光、进行图像分析，并通过语音合成反馈结果。
    - 您可以通过语音输入其他指令，程序将根据指令进行处理。

## 许可

本项目使用 [MIT 许可证](https://opensource.org/licenses/MIT)。请查看 [LICENSE](https://github.com/2642086672/Camra-GPT/blob/main/LICENSE) 文件了解更多信息。

## 外部链接

- [OpenAI API 文档](https://beta.openai.com/docs/)
- [OpenCV 文档](https://docs.opencv.org/)
- [Pyttsx3 文档](https://pyttsx3.readthedocs.io/en/latest/)
- [SpeechRecognition 文档](https://pypi.org/project/SpeechRecognition/)
