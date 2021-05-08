# Sample code to run detectron using webcam  
This is a very simple code to run [Detectron](https://github.com/facebookresearch/Detectron) Mask RCNN using webcam.  
Place infer_simple.py file in  /detectron/tools/ and vis.py file in /detectron/lib/utils/ folder.  
The code to run the test is the same as it is mentioned in [this](https://github.com/facebookresearch/Detectron/blob/master/GETTING_STARTED.md) website.  

```
python2 tools/infer_simple.py \
    --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml \
    --output-dir /tmp/detectron-visualizations \
    --image-ext jpg \
    --wts https://s3-us-west-2.amazonaws.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
    demo
```

The code was tested successfully in  
* Ubuntu 16.04  
* Cuda 8.0  
* CUDNN 6  
* opencv 3.4  






