import os
import cv2

dataset_dir = 'UG2_haze'

haze_dir = os.path.join(dataset_dir, 'haze_images')

# 读取haze_images文件夹下的所有图片文件名
image_names = os.listdir(haze_dir)

# 遍历每张图片，进行上下分割并保存
for image_name in image_names:
    # 读取原始图片
    image_path = os.path.join(haze_dir, image_name)
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # 计算上下分割线的位置
    # height, width = img.shape[:2]
    # split_line = int(height / 2)
    
    # 上下分割
    top_img = img[:750, :]
    bottom_img = img[750:, :]
    
    # 保存分割后的两张图片
    top_dir = os.path.join(dataset_dir, 'haze_images_top')
    bottom_dir = os.path.join(dataset_dir, 'haze_images_bottom')
    if not os.path.exists(top_dir):
        os.makedirs(top_dir)
    if not os.path.exists(bottom_dir):
        os.makedirs(bottom_dir)
    top_img_path = os.path.join(top_dir, image_name)
    bottom_img_path = os.path.join(bottom_dir, image_name)
    cv2.imwrite(top_img_path, top_img)
    cv2.imwrite(bottom_img_path, bottom_img)
