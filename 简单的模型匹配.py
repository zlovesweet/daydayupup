import cv2
import pyautogui
import pyscreeze

# 屏幕缩放系数 mac缩放是2 windows一般是1
screenScale = 1
img_path = r'./xx.png'
confidence = 0.9  # 匹配置信度
# 截取桌面
pyscreeze.screenshot('temp_screenshot/desktop.png')
# 读取图片,灰度图
desktop = cv2.imread(r'temp_screenshot/desktop.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
theight, twidth = img.shape[:2]
tempheight, tempwidth = desktop.shape[:2]
print("目标图宽高：" + str(twidth) + "-" + str(theight))
print("模板图宽高：" + str(tempwidth) + "-" + str(tempheight))
# 先缩放屏幕截图 INTER_LINEAR INTER_AREA
scaleTemp = cv2.resize(desktop, (int(tempwidth / screenScale), int(tempheight / screenScale)))
stempheight, stempwidth = scaleTemp.shape[:2]
print("缩放后模板图宽高：" + str(stempwidth) + "-" + str(stempheight))

# 匹配图片
res = cv2.matchTemplate(scaleTemp, img, cv2.TM_CCOEFF_NORMED)
mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(f"匹配最高置信度：{max_val}")
if max_val >= confidence:
    print(f'目标图在模板图上的起始坐标(左上){max_loc}')
    tagHalfW = int(twidth / 2)
    tagHalfH = int(theight / 2)
    tagCenterX = max_val[0] + tagHalfW
    tagCenterY = max_val[1] + tagHalfH
    print(f'图像中心点：{tagCenterX, tagCenterY}')
    # 左键点击屏幕上的这个位置
    # pyautogui.click(tagCenterX, tagCenterY, button='left')
    # 鼠标移动到屏幕上的这个位置
    pyautogui.moveTo(tagCenterX, tagCenterY, )

else:
    print(f'未找到图像，最高置信度：{max_val}')
