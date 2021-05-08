train dataset: VOC 2012 + VOC 2007<br>
test size: 544<br>
test code: [Faster rcnn](https://github.com/rbgirshick/py-faster-rcnn/blob/master/lib/datasets/voc_eval.py) (not use 07 metric)<br>
test GPU: 12G 2080Ti<br>
test CPU: E5-2678 v3 @ 2.50GHz
<table>
   <tr><td>Version</td><td>Network</td><td>Backbone</td><td>Initial weight</td><td>VOC2007 Test(mAP)</td><td>Inference(GPU)</td><td>Inference(CPU)</td><td>Params</td></tr>
   <tr><td>V1</td><td>YOLOV3</td><td>Darknet53</td><td>YOLOV3-608.weights</td><td>88.8</td><td>30.0ms</td><td>255.8ms</td><td>248M</td></tr>
   <tr><td>V2</td><td>YOLOV3</td><td>Darknet53</td><td>Darknet53_448.weights</td><td>83.3</td><td>30.0ms</td><td>255.8ms</td><td>248M</td></tr>
   <tr><td>V3</td><td>YOLOV3-Lite</td><td>MobilenetV2</td><td>MobilenetV2_1.0_224.ckpt</td><td>79.4</td><td>18.9ms</td><td>80.9ms</td><td>27.3M</td></tr>
</table>

Check [Strongeryolo-pytorch](https://github.com/wlguan/Stronger-yolo-pytorch) for **pytorch** version with channel-pruning.  
There is also a [MNN Demo](https://github.com/wlguan/MNN-yolov3) for Verson V3. 
