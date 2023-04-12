import os
import json
import argparse

parser = argparse.ArgumentParser(description='Convert detection annotations to COCO format')
parser.add_argument('--anno_dir', type=str, default="UG2_haze/haze_images_labels",
                    help='Path to folder containing detection annotations in format "vehicle x y w h"')
parser.add_argument('--json_file_name', type=str, default='haze_images_labels_coco.json',
                    help='Path to output COCO format annotations file')
args = parser.parse_args()

# anno_dir = "UG2_haze/haze_images_labels"
anno_dir = args.anno_dir

# 定义类别名称和ID的映射关系
categories = {"vehicle": 1}

# 遍历所有标注文件
anns = []
for txt_file in os.listdir(anno_dir):
    with open(os.path.join(anno_dir, txt_file), 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        items = line.strip().split()
        category_name = items[0]
        x, y, w, h = map(int, items[1:])

        # 构造COCO格式的检测框
        ann = {}
        ann['image_id'] = txt_file.split('.')[0]  # 标注文件名对应的图像ID
        ann['category_id'] = categories[category_name]  # 目标类别ID
        ann['bbox'] = [x, y, w, h]  # 检测框坐标
        ann['score'] = 1.0  # 假设检测得分为1.0

        anns.append(ann)

# 将所有标注信息转换为JSON字符串
json_str = json.dumps(anns)

# 将JSON字符串写入文件
with open(os.path.join(anno_dir, args.json_file_name), 'w') as f:
    f.write(json_str)
