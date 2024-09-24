import cv2
import base64

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

def capture_image_from_camera():
    """从摄像头捕捉图像并保存为文件"""
    cap = cv2.VideoCapture(0)  # 打开默认摄像头
    if not cap.isOpened():
        print("无法打开摄像头")
        return None

    # 调整曝光设置
    adjust_exposure(cap)

    print("请对着摄像头...")
    ret, frame = cap.read()  # 捕捉一帧
    cap.release()  # 释放摄像头

    if ret:
        image_path = '/Users/meikailong/Downloads/A.jpeg'  # 更新为所需的图像保存路径
        cv2.imwrite(image_path, frame)  # 保存图像
        print(f"图像已保存为 {image_path}")
        return image_path
    else:
        print("无法捕捉图像")
        return None

def image_to_base64(image_path):
    """将图像转换为 base64 编码"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')