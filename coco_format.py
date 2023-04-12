import os
import json

def convert_to_coco(img_dir, label_dir):
    categories = [{'id': 0, 'name': 'vehicle'}]
    images = []
    annotations = []
    image_id = 0
    annotation_id = 0
    
    for filename in os.listdir(label_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(label_dir, filename)
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            image_name = os.path.splitext(filename)[0] + '.jpg'
            image_path = os.path.join(img_dir, image_name)
            image = {'file_name': image_name}
            
            # Get image size using OpenCV
            import cv2
            img = cv2.imread(image_path)
            height, width, _ = img.shape
            image.update({'height': height, 'width': width, 'id': image_id})
            images.append(image)
            
            for line in lines:
                # Parse label format: vehicle 619 0 777 135
                label, x1, y1, x2, y2 = line.strip().split()
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Calculate bbox coordinates
                bbox_width = x2 - x1
                bbox_height = y2 - y1
                bbox = [x1, y1, bbox_width, bbox_height]
                
                # Create annotation object
                annotation = {
                    'segmentation': [],
                    'area': bbox_width * bbox_height,
                    'iscrowd': 0,
                    'image_id': image_id,
                    'bbox': bbox,
                    'category_id': 0,
                    'id': annotation_id
                }
                
                annotations.append(annotation)
                annotation_id += 1
            
            image_id += 1
            
    result = {'images': images, 'annotations': annotations, 'categories': categories}
    
    with open(os.path.join(label_dir, 'coco_format.json'), 'w') as f:
        json.dump(result, f)

dataset_dir = 'UG2_haze'

img_dir = os.path.join(dataset_dir, 'haze_images')

label_dir = os.path.join(dataset_dir, 'haze_images_labels')


convert_to_coco(img_dir, label_dir)