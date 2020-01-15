# config.py
import os.path

# for making bounding boxes pretty
COLORS = ((255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128),
          (0, 255, 255, 128), (255, 0, 255, 128), (255, 255, 0, 128))
MEANS = (104, 117, 123)
# ANCHOR SIZE is from the anchor config of YOLO-v2. But, following is searched by myself!!!
ANCHOR_SIZE = [[1.19, 1.98], [2.79, 4.59], [4.53, 8.92], [8.06, 5.29], [10.32, 10.65]] 
      
# ANCHOR_SIZE_COCO = [[0.53, 0.79], [1.71, 2.36], [2.89, 6.44], [6.33, 3.79], [9.03, 9.75]]

IGNORE_THRESH = 0.5


# yolo-v2 config
voc_ab = {
    'num_classes': 20,
    'lr_epoch': (150, 200, 250),
    'max_epoch': 250,
    'min_dim': [608, 608],
    'ms_channels':[128, 256, 512],
    'stride': 32,
    'strides': [16, 32],
    'multi_scale': [[320, 320], [352, 352], [384, 384], [416, 416], [448, 448],
                 [480, 480], [512, 512], [544, 544], [576, 576], [608, 608]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'VOC',
}

coco_ab = {
    'num_classes': 80,
    'lr_epoch': (150, 200, 250),
    'max_epoch': 250,
    'min_dim': [416, 416],
    'ms_channels':[128, 256, 512],
    'stride': 32,
    'strides': [16, 32],
    'multi_scale': [[320, 320], [352, 352], [384, 384], [416, 416], [448, 448],
                 [480, 480], [512, 512], [544, 544], [576, 576], [608, 608]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'COCO',
}

imagenet = {
    'batch_size': 64,
    'resize': 448,
    'max_epoch': 10,
    'lr': 1e-3,
    'data_path': "/home/k545/object-detection/myYOLO/backbone/imagenet/",
    'model_name': 'darknet19'
}