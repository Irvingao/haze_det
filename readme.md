

## create dataset

### UG2
```bash
ln -s /home/gaohz/dataset/UG2_haze ./
```

```bash
python data_split.py
python anno_converter.py
```

### DOTA-v1.0

```bash
git clone https://github.com/dingjiansw101/AerialDetection.git

# create coco dataset
python DOTA_devkit/prepare_dota1.py --srcpath /dataset/DOTA-v1.0 --dstpath /dataset/DOTA-v1.0
```



## mmdet

```bash
git clone https://github.com/open-mmlab/mmdetection.git

```


## Train

```bash
python tools/train.py configs/point_rend/point_rend_r50_caffe_fpn_mstrain_1x_coco.py
```

- training with multi-GPU:
```bash
bash tools/dist_train.sh configs/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_20e_coco.py 2

CUDA_VISIBLE_DEVICES=1 PORT=29505 bash tools/dist_train.sh configs/cascade_rcnn_dota/cascade_rcnn_r50_fpn_20e_coco_dota1.py 1


```


