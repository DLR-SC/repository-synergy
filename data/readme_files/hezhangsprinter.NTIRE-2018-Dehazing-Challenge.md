## Multi-scale Single Image Dehazing using Perceptual Pyramid Deep Network (NTIRE-2018-Dehazing-Challenge)
[He Zhang](https://sites.google.com/site/hezhangsprinter), [Vishwanath Sindagi](http://www.vishwanathsindagi.com/), [Vishal M. Patel](http://www.rci.rutgers.edu/~vmp93/)

**This method rank 1st place in the indoor track and 3rd place in the outdoor track in [NTIRE-2018 Dehazing Challenge](http://www.vision.ee.ethz.ch/en/ntire18/).**



[Paper Link](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w13/Zhang_Multi-Scale_Single_Image_CVPR_2018_paper.pdf) (CVPRw'18)

Haze adversely degrades quality of an image thereby affecting its aesthetic appeal and visibility in outdoor scenes. Single image dehazing is particularly challenging due to its ill-posed nature. Most existing work, including the recent convolutional neural network (CNN) based methods, rely on the classical mathematical formulation where the hazy image is modeled as the superposition of attenuated scene radiance and the atmospheric light. In this work, we explore CNNs to directly learn a non-linear function between hazy images and the corresponding clear images. We present a multi-scale image dehazing method using Perceptual Pyramid Deep Network based on the recently popular dense blocks and residual blocks. The proposed method involves an encoder-decoder structure with a pyramid pooling module in the decoder to incorporate contextual information of the scene while decoding. The network is learned by minimizing the mean squared error and perceptual losses. Multi-scale patches are used during training and inference process to further improve the performance. Experiments on the recently released NTIRE2018-Dehazing dataset demonstrates the superior performance of the proposed method over recent state-of-the-art approaches. Additionally, the proposed method is ranked among top-3 methods in terms of quantitative performance in the recently conducted NTIRE2018-Dehazing challenge.

	@inproceedings{dehaze_zhang_2018w,		
	  title={Multi-scale Single Image Dehazing using Perceptual Pyramid Deep Network},
	  author={Zhang, He and Sindagi, Vishwanath and Patel, Vishal M},
	  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
	  year={2018}
	} 


And this method rank 1st in the indoor track and 3rd in the outdoor track in [NTIRE-2018 Dehazing Challenge](http://www.vision.ee.ethz.ch/en/ntire18/) (CVPRw'18). 

Install pytorch with 0.3.x rather than the latest 0.4.x version.


All the codes can be also be found in the following link
https://drive.google.com/drive/folders/1BjJDM7qCdgqSR356PHcSUi_6fWclrGad?usp=sharing
