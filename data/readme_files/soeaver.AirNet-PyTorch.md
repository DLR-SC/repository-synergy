# AirNet-PyTorch
Implementation of the paper ''Attention Inspiring Receptive-fields Network'' (under review), which contains the evaluation code and trained models. By:

[Lu Yang](https://github.com/soeaver), Qing Song, Yingqi Wu and Mengjie Hu

<p align="center">
<img src="https://github.com/soeaver/AirNet-PyTorch/blob/master/images/air_bottleneck.png" height="320">
<img src="https://github.com/soeaver/AirNet-PyTorch/blob/master/images/air_module.png" height="320">
</p>


## Install
* Install [PyTorch>=0.3.0](http://pytorch.org/)
* Install [torchvision>=0.2.0](http://pytorch.org/)
* Clone
  ```
  git clone https://github.com/soeaver/AirNet-PyTorch
  ```

## Evaluation
* Download the trained models, and move them to the `ckpts` folder.
* Run the `eval.py`:
  ```
  python eval.py --gpu_id 0 --arch airnet50_1x64d --model_weights ./ckpts/air50_1x64d.pth
  ```
* The results will be consistent with the paper.


## Results

### ImageNet1k
Single-crop (224x224) validation error rate is reported. 

| Network                 | Flops (G) | Params (M) | Top-1 Error (%) | Top-5 Error (%) | Download |
| :---------------------: | --------- |----------- | --------------- | --------------- | -------- |
| AirNet50-1x64d (r=16)   | 4.36      | 25.7       | 22.11           | 6.18            | [GoogleDrive](https://drive.google.com/open?id=1oUHnx8pw9YRJshN2biLoh_H1I4efoTWE) |
| AirNet50-1x64d (r=2)    | 4.72      | 27.4       | 21.83           | 5.89            | [GoogleDrive](https://drive.google.com/open?id=1rOA9ciKbEKMkiDO3g3qY06goXZR9hO-Y) |
| AirNeXt50-32x4d         | 5.29      | 25.5       | 20.87           | 5.52            | [GoogleDrive](https://drive.google.com/open?id=1xLcPHN1NCONtpDKNXDEIKhAn475mYD-L) |


## Other Resources (from [DPNs](https://github.com/cypw/DPNs))

ImageNet-1k Trainig/Validation List:
- Download link: [GoogleDrive](https://goo.gl/Ne42bM)

ImageNet-1k category name mapping table:
- Download link: [GoogleDrive](https://goo.gl/YTAED5)

