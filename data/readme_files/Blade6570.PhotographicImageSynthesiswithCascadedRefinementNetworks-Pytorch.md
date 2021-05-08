# Photographic Image Synthesis with Cascaded Refinement Networks-Pytorch (https://arxiv.org/abs/1707.09405)
This is a Pytorch implementation of cascaded refinement networks to synthesize photographic images from semantic layouts. Now the pretrained model and codes for training the network from scratch are available for 256x512 resolution. Thanks to [Qifeng Chen](https://github.com/CQFIO) for his tensorflow implementation which helped a lot in developing this pytorch version. 
![Output](https://github.com/Blade6570/Photographic-Image-Synthesis-with-Cascaded-Refinement-Networks--Pytorch-/blob/master/Screenshot_from.png?raw=true "Comparision with Original TensorFlow version")

**Testing**
1. Download this package and keep all the subsequent mentioned files in the same folder.
2. Download the pretrained VGG19 Net from [VGG19](https://drive.google.com/open?id=1wkMhYoRdjZ7LC1OeTOIdzf5YcxNvR8vs)
3. Download the pretrained weights for the CRN network for 256x512 [CRN](https://drive.google.com/open?id=1WHPMDLkRvQMKRoHhV8-tqFhZgmOfoA3p)
4. Keep the *mode=test* and mention the semantic image name to be tested in the *Cascadaed_Network_LM_256.py*
5. The synthesized images will be saved in current folder.

 **Training**
 1. Follow steps *1 to 3* from the testing steps.
 2. Resize all the training images to 256x512. Keep the semantic segmentated training images in *Label256Full* folder and     
    the RGB training images in *RGB256Full* (without any subfolders).
 3. Set *mode=train* in *Cascadaed_Network_LM_256.py* and run it for desired epochs (default is 200).
 
 **Future Work**
 1. Soon the pretrained weights for resolution *512x1024* and *1024x20148* will be available along with training scripts. 
 
 **Note**
 1. All the codes are written to run on GPU. Suitable changes should be done if you want to run on CPU. Also feel free to   
    customize it according to your need.
