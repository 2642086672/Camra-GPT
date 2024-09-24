import cv2
import base64

def adjust_exposure(cap):
    """调整摄像头的曝光设置"""
    exposure_value = -4
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure_value)
    print(f"初始曝光值: {exposure_value}")

    for _ in range(10):
        cap.set(cv2.CAP_PROP_EXPOSURE, exposure_value)
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Exposure Adjustment", frame)
            print(f"当前曝光值: {exposure_value}")
            key = cv2.waitKey(1000)
            if key == 27:
                break
        exposure_value += 1

    cv2.destroyAllWindows()

def capture_image_from_camera():
    """从摄像头捕捉图像并保存为文件"""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return None

    adjust_exposure(cap)

    print("请对着摄像头...")
    ret, frame = cap.read()
    cap.release()

    if ret:
        image_path = '/Users/meikailong/Downloads/A.jpeg'
        cv2.imwrite(image_path, frame)
        print(f"图像已保存为 {image_path}")
        return image_path
    else:
        print("无法捕捉图像")
        return None

def image_to_base64(image_path):
    """将图像转换为 base64 编码"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

